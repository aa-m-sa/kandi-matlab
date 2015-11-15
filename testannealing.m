% test annealing (multiple runs with same data)
% write results to file
% also generate pictures

% quite slow!

clear all;
close all;

% image size
N = 200;

% params for data circle
% kuvat 1
% params = [10 10 7; 5 20 15; 46 50 10; 0 8 14];
% kuvat 2
numPics = 4

pic1 = [40 40 50]
pic2 = [100 70 30]
pic3 = [80 140 90]
pic4 = [170 160 25];
picSets = {pic1; pic2; pic3; pic4};
for picInd = 1:numPics
    clf;
    picSet = picSets(picInd){:};
    x = picSet(:, 1);
    y = picSet(:, 2);
    r = picSet(:, 3);

    A = circle(x, y, r, [N N], 0);
    I = convolution(A);
    I_noise = addnoise(I);

    subpics = 3
    subplot(2, subpics, 1);
    imshow(I_noise)
    hold on;

    for pic = 1:3
        [xa, ya, ra, aDataPts, aDataR] = annealing(I_noise, 1);

        % only one circle, so we can do this
        annPlot = flipud(aDataPts);

        subplot(2,subpics,subpics+pic)
        imshow(I_noise);
        hold on;
        % plot progress
        plot(annPlot(1,:), annPlot(2,:), 'linewidth', 1)
        % plot final result
        plot(ya, xa, 'r.', 'markersize', 4)

        % plot progress circles
        t = repmat(linspace(0, 2*pi, 100)', 1, columns(annPlot));
        cr = repmat(aDataR', rows(t), 1);
        cntx = repmat(annPlot(1, :), rows(t), 1);
        cnty = repmat(annPlot(2, :), rows(t), 1);
        cx = cr.*sin(t) + cntx;
        cy = cr.*cos(t) + cnty;
        plot(cx, cy, 'g', 'linewidth', 1)

        % result circle
        rt = linspace(0, 2*pi, 100);
        plot(ra*sin(rt) + ya, ra*cos(rt) + xa, 'r', 'linewidth', 1);
    end

    print(['testann-2014-12-05-uusi-n1-' num2str(picInd) '.png'], '-dpng')
end
