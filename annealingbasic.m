% function file for annealing algorithm
% the basic version for a test run

function [x, y, r, annDataPoints, annDataRadii, annDataEnergies, annDataTemps, ratios] = annealingbasic(data, nCircles)
    % ANNEALING uses simulated annealing algorithm to find best fit for
    % a fixed number of 1-circles in a image data matrix
    %
    % params:
    % data: image data matrix
    % nCircles: number of circles (parameter vectors x, y, r)
    %
    % returns:
    %
    % x, y, r: locations, radii of the circles found
    % annDataPoints, Radii: locations, radii of circles after each Markov chain
    % annDataTemps: the corresponding temperature values used
    % annDataEnergies: the corresponding values of energy function

    datasize = size(data); N = datasize(1); M = datasize(2);

    % fuzzy logic to deduce what params have been given:
    if nargin == 1
        % nCircles not specified
        nCircles = 1;
    end
    % pick the initial state x0, y0, r0
    % large r that first circles will cover a sizeable part of image
    r = initialradius(N, M, nCircles);
    [x, y] = initialcoord(N, M, nCircles);

    % initial energy = cost
    e = cost(x, y, r, data);
    ePrev  = 0;
    ePrev2 = 0;
    eBest = e;

    % adjust temp so that the prob associated with the
    % 'initial mean energy delta' is close enough to 1
    t = initialtemp(x, y, r, N, M, data);

    % keep tally of acceptance ratio (for adjusting the initial t)
    accepted = 0;
    transitions = 0;

    n = 300;     % how many times temp is decreased?
    k = 1;

    % fixed markov chain length
    l = 10;
    disp('start')
    % when ratios get low -> virtually no new accepted transitions
    while k < n && (k < 5 || sum(ratios(k-4:k-1)) > 0.2)
        acceptedOld = accepted;
        transitionsOld = transitions;
        ePrev2 = ePrev;
        ePrev = e;
        for i = 1:l     % some fixed markov chain length l
            transitions = transitions + 1;
            [xNew, yNew, rNew] = transition(x, y, r, N, M);
            eNew = cost(xNew, yNew, rNew, data);
            if prob(eNew, e, t) > rand
                % accept if eNew is better;
                % Metropolis criterion (SA main idea):
                % => randomly accept some anyway
                e = eNew;
                x = xNew;
                y = yNew;
                r = rNew;
                accepted = accepted + 1;
            end
        end

        annDataPoints(1,k,:) = x;
        annDataPoints(2,k,:) = y;
        annDataRadii(k, :) = r;
        annDataTemps(k) = t;
        annDataEnergies(k) = e;
        ratios(k) = (accepted - acceptedOld) / (transitions - transitionsOld);
        %disp(accepted/transitions)
        %disp(ratios(k))
        %disp(' ')

        if e <= eBest
            eBest = e;
        end

        k = k + 1;
        t = temperature(t);
    end

    disp('Annealing end condition met:')
    if k == n
        disp('(Time limit exceeded)')
    end
    disp('Number of Markov chains:')
    disp(k)
    disp('Final energy:')
    disp(e)
    disp('Circles found:')
    disp([x, y, r])

end

function y = cost(x, y, r, data)
    % COST returns the value of the cost function (energy function) for
    % given state (= params x, y, r). In practice, the cost function is
    % the norm of difference between the image matrix and matrix created with
    % the given set of parametres.

    datasize = size(data);
    N = datasize(1);
    M = datasize(2);

    A = circle(x, y, r, [N, M], 0, 1);
    I = convolution(A);
    % noise not necessary?
    %I_noise = addnoise(I);

    % our norm is \sigma_i \sigma_j |a(i,j)|^2 (Frobenius without sqrt)
    % can be calculated easily with a little matrix wizardry:

    d = I - data;
    y = sum(diag(d' * d));
    %y = norm(d, 'fro');
    % in theory octave/matlab frobenius might be faster? in practise, doesn't
    % seem so

    % ^ the above method has some problems:
    % if the param circle and data circle don't overlap, it doesn't
    % distinguish two param sets even if another is much more 'close' to
    % data circle than another

end

function r = initialradius(N, M, nCircles)
    % picks the initial radii (nCircles x 1 vector)

    % first radii should cover a significant part of image data
    % ...but not overlap too much
    r = min(N/(3 * nCircles), M/(3 * nCircles));
    r = repmat(r, nCircles, 1);
end

function [x, y] = initialcoord(N, M, nCircles)
    % picks the initial coordinates x, y

    % naive: random
    x = ceil(N*rand(nCircles, 1));
    y = ceil(M*rand(nCircles, 1));
end

function t = initialtemp(x, y, r, N, M, data)
    % picks the initial temperature
    % method: do some random transitions and calculate their respective energy
    % values.  Use them to estimate the mean energy difference, and pick such a
    % temperature that near ~all of transitions will be accepted.
    e = cost(x, y, r, data);
    for ti = 1:10
        [x y r] = transition(x, y, r, N, M);
        eInits(ti) = cost(x, y, r, data);
    end

    eDiffs = abs(eInits(1) - e);
    count = 1;
    % ^ prevent divide by zero

    for i = 2:length(eInits)
        if eInits(i) - eInits(i-1) > 0
            eDiffs = eDiffs + eInits(i) - eInits(i-1);
            count = count + 1;
        end
    end

    % mean of energy differences for transitions ti
    eMean = eDiffs/count
    % q_0 ~ 1, the accepted / all transitions ratio we want for init temp
    q_0 = 0.9
    pr = -log(q_0)
    t = ceil(eMean / pr)
end

function tnew = temperature(told)
    % TEMPERATURE is used to decrement temperature (control parameter)
    % tnew = a*told, for some fixed a < 1

    a = 0.98;

    tnew = a.*told;

end

function [xnew, ynew, rnew] = transition(x, y, r, N, M)
    % TRANSITION picks up a new circle configuration near the original x, y, r

    % delta is the amount of change / transition distance
    % if too small, takes too much time to find the circle in data; if too large, very imprecise
    delta = max(M/15, N/15);     % a guess

    % move just one circle at time
    toMove = ceil(length(x)*rand);

    % pick a new random r within delta from old of old r
    baseChange = 2*rand - 1;
    rnew = r;
    rnew(toMove) = abs(delta*baseChange + r(toMove));
    % but don't allow it to get too small or large
    ri = rnew < max(N, M) / 50 | rnew > max(N, M);
    rnew(ri) = r(ri);

    % pick a random direction
    dir = 2*pi*rand;
    dx = delta * cos(dir);
    dy = delta * sin(dir);

    xnew = x;
    ynew = y;
    xnew(toMove) = round(x(toMove) + dx);
    ynew(toMove) = round(y(toMove) + dy);

    % instead of torus, boundaries
    xis = xnew <= 0;
    xnew(xis) = 1;
    xil = xnew > N;
    xnew(xil) = N;

    yis = ynew <= 0;
    ynew(yis) = 1;
    yil = ynew > N;
    ynew(yil) = N;
end

function y = prob(eNew, eOld, t)
    % PROB the Metropolis criterion

    % notice that if eNew < eOld, y > 1
    y = exp(-(eNew - eOld)/t);
end
