% script to plot various energy functions

% image size

N = 200;

x1 = 60
y1 = 120
r1 = 40

A1 = circle(x1, y1, r1, [N N], 0);
I1 = convolution(A1);
I_data = addnoise(I1);

[X, Y] = meshgrid(1:N);

for r = 10:10:60
    for x = 1:N
        for y = 1:N
            A = circle(x, y, r, [N, N], 0);
            I = convolution(A);
            d = I - I_data;
            z = sum(diag(d' * d));
            Z(x, y) = z;
        end
    end
    clf;
    %colormap(gray)
    surfc(X, Y, Z)
    axis([0 200 0 200 0 14000])
    title(['r = ' num2str(r)])
    print(['energyf-2014-11-23-3-r' num2str(r) '.png'], '-dpng')
end
