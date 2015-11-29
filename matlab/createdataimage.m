
function I = createdataimage(x, y, r, N, M)
    % CREATEDATA(x, y, r, N, M) creates simulated test circle image data:
    % creates filled 1-circles in an image matrix, applied a convolution filter
    % (imfilter) and then applies some uniform noise.
    %
    % params x, y, r specify location and radii of the circles
    % params N, M specify image matrix size
    A = circle(x, y, r, [N M], 0);
    F = [0 1 1 1 0; 1 2 2 2 1; 1 2 8 2 1; 1 2 2 2 1; 0 1 1 1 0]./36;
    C = imfilter(double(A), F, 'replicate', 'conv');
    I = addnoise(C);
end
