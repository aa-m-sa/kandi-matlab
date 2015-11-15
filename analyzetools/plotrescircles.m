% function for plotting candidate circles
% (in the current figure)

function plotrescircles(xa, ya, ra)

    plot(ya, xa, 'r.', 'markersize', 4)
    rt = linspace(0, 2*pi, 100);
    for circ = 1:length(ya)
        plot(ra(circ)*sin(rt) + ya(circ), ra(circ)*cos(rt) + xa(circ), ...
        'r', 'linewidth', 2);
    end

end
