
function I = convolution(A, options)
    % CONVOLUTION applies a certain 2-d convolution effect to image.
    % Used for objective function image model.
    %
    % Uses Octave (or Matlab) function imfilter.
    % Optional param 'options' is an options string passed to imfilter; if
    % left unspecified, 'replicate' is used.

    if nargin < 2
        options = 'replicate';
    end

    % convolution matrix P
    P = [2 2 2; 2 10 2; 2 2 2] ./26;

    I = imfilter(double(A), P, options, 'conv');

end
