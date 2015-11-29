

function I = addnoise(A)
    % ADDNOISE adds some predetermined white noise to image matrix A

    % pick up uniform random matrix U(-0.5, 0.5), sum that with A

    R = rand(size(A)) - 0.5;

    I = A + R;

    % "cut off" the values of A outside the limits [0, 1] so that
    % the matrix remains a greyscale image
    % (I don't actually know if this is mathematically sound or even
    % necessary, but it feels sensible thing to do.
    % I guess the other option would be to scale the resulting image
    % "[-0.5, 1.5] -> [0, 1]")

    I(I < 0) = 0;
    I(I > 1) = 1;

end
