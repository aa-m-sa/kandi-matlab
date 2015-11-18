function [xnew, ynew, rnew] = basictransition(x, y, r, N, M, varargin)
    % BASICTRANSITION picks up a new circle configuration near the original x, y, r
    %
    % BASICTRANSITION(x, y, r, N, M)
    % BASICTRANSITION(x, y, r, N, M, delta)
    %
    % delta is the amount of change / transition distance
    % if too small, takes too much time to find the circle in data;
    % if too large -> algorithm very imprecise
    if length(varargin) == 0
        delta = max(M/15, N/15);     % a default guess
    else
        delta = varargin{1};         % use delta given as param
    end

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
