function A = circle(x, y, radius, dimensions, torus, overlapsum)
    % CIRCLE creates a greyscale image matrix representing a solid disk
    % that is centered at (x,y) and has specified radius.
    %
    % Dimensions is [M, N] vector that specifies the dimensions of the
    % resulting matrix A.
    %
    % The pixel A(i,j) will be 0 if it's contained in the circle, 1 otherwise.
    % for now, x, y should be matrix coordinates (i.e. integers)
    %
    % Optional argument 'torus' specifies whether to treat the image as a torus
    % surface. Default is 0 (no).
    %
    % If argument 'overlapsum' is 1, overlapping circles will be negative
    % (e.g. -1 if the pixel is contained in two circles, -2 if three, etc.)

    M = dimensions(1);
    N = dimensions(2);

    if nargin < 6
        torus = 0;
        overlapsum = 0;
    end

    [meshN meshM] = meshgrid(1:N, 1:M);

    if overlapsum == 0
        circleMask = mask(meshM, meshN, x, y, radius);
        A = ~circleMask;
    else
        A = summask(meshM, meshN, x, y, radius);
    end

end

function A = mask(meshM, meshN, x, y, radius)
    % try to optimize this (matrix op?)
    A = zeros(size(meshM));
    for i = 1:length(x)
        A = A | (meshM - x(i)).^2 + (meshN - y(i)).^2 <= radius(i).^2;
    end
end

function A = summask(meshM, meshN, x, y, radius)
    % try to optimize this (matrix op?)
    A = ones(size(meshM));
    for i = 1:length(x)
        A = A - ((meshM - x(i)).^2 + (meshN - y(i)).^2 <= radius(i).^2);
    end
end
