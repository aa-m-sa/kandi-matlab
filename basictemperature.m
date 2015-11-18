function tnew = basictemperature(told, varargin)
    % BASICTEMPERATURE is used to decrement temperature (control parameter)
    % tnew = a*told, for some fixed a < 1
    % BASICTEMPERATURE(told)
    % BASICTEMPERATURE(told, a)

    if length(varargin) == 0
        a = 0.98;
    else
        a = varargin{1};
    end

    tnew = a.*told;

end


