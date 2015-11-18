function y = basiccost(x, y, r, data, torus, overlapsum)
    % BASICCOST a basic cost function that returns the value of the cost
    % function (energy function) for given state (= params x, y, r). In
    % practice, the cost function is
    % the norm of difference between the image matrix and matrix created with
    % the given set of parametres.
    %
    % params torus, overlapsum passed to circle.m
    %

    datasize = size(data);
    N = datasize(1);
    M = datasize(2);

    A = circle(x, y, r, [N, M], torus, overlapsum);
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
