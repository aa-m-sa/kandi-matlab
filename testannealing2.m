% testannealing2.m
% test script for testing the annealing procedure for multiple (fixed number of) disks

clear all;
close all;

% image size
N = 200;

% params for circles in pics
numPics = 5
pic1 = [60 120 40];
pic2 = [40 30 20; 150 130 45];
pic3 = [50 50 25; 150 110 40; 80 140 15];
pic4 = [20 30 15; 130 20 10; 90 80 50; 180 170 15];
pic5 = [15 10 5; 160 150 30; 80 50 40; 170 20 10; 70 140 25];

picSets = {pic1; pic2; pic3; pic4; pic5};

for picInd = 1:numPics
    clf;
    picSet = picSets(picInd);
    picSet = picSet{:}
    x = picSet(:, 1);
    y = picSet(:, 2);
    r = picSet(:, 3);

    A_data = createdataimage(x, y, r, N, N);

    subpics = 3
    subplot(2, subpics, 1);
    imshow(A_data)
    hold on;
    for pic = 1:subpics

        [xa, ya, ra, aDataPts, aDataR] = annealing(A_data, picInd);

        %annPlot = flipud(aDataPts);

        subplot(2,subpics,subpics+pic)
        imshow(A_data);
        hold on;

        % plot progress
        %plot(annPlot(1,:), annPlot(2,:), 'linewidth', 1)
        %for p = 1:3
        %    xPtsData = aDataPts(1, :, p);
        %    yPtsData = aDataPts(2, :, p);
        %    plot(yPtsData, xPtsData, 'linewidth', 1)
        %end
        % plot final result
        plot(ya, xa, 'r.', 'markersize', 4)

        % plot progress circles
        %t = repmat(linspace(0, 2*pi, 100)', 1, columns(annPlot));
        %cr = repmat(aDataR, rows(t), 1);
        %cntx = repmat(annPlot(1, :), rows(t), 1);
        %cnty = repmat(annPlot(2, :), rows(t), 1);
        %cx = cr.*sin(t) + cntx;
        %cy = cr.*cos(t) + cnty;
        %plot(cx, cy, 'g', 'linewidth', 1)

        % result circle
        rt = linspace(0, 2*pi, 100);
        for k = 1:length(ya)
            plot(ra(k)*sin(rt) + ya(k), ra(k)*cos(rt) + xa(k), 'r', 'linewidth', 2);
        end
    end

    % pr 0.2, markov len 10
    %print(['testann-2014-11-20-multi-t2-n3-a' num2str(picInd) '.png'], '-dpng')

    % pr 0.1, markov len 10*nCircles
    %print(['testann-2014-11-20-multi-t2-n3-b3' num2str(picInd) '.png'], '-dpng')

    % ^ but also t = 0.98t instead 0.95
    %print(['testann-2014-11-20-multi-t2-n3-c1' num2str(picInd) '.png'], '-dpng')
    % + new cutoff

    % new cutoff, n = 200, l = 10
    %print(['testann-2014-11-20-multi-t2-n3-d1' num2str(picInd) '.png'], '-dpng')
    % min r
    %print(['testann-2014-11-20-multi-t2-n3-d2' num2str(picInd) '.png'], '-dpng')

    % refined cutoff
    %print(['testann-2014-11-20-multi-t2-n3-e2' num2str(picInd) '.png'], '-dpng')

    % refined min r, also max r
    %print(['testann-2014-11-20-multi-t2-n3-e2b1' num2str(picInd) '.png'], '-dpng')
    % larger min r
    %print(['testann-2014-11-20-multi-t2-n3-e2b2' num2str(picInd) '.png'], '-dpng')

    % markov chain = 10*nCircles + n = 300
    %print(['testann-2014-11-20-multi-t2-n3-f1b4' num2str(picInd) '.png'], '-dpng')

    % short l
    %print(['testann-2014-11-20-multi-t2-n3-f1c2' num2str(picInd) '.png'], '-dpng')

    % hypothesis: trying to move all circles randomly per transition not ideal:
    % maybe transition that might get some of the other circles out of local min
    % towards the global min would too easily get the already found big circle
    % moving too?

    %print(['testann-2014-11-20-multi-t2-n3-g1a2' num2str(picInd) '.png'], '-dpng')
    % no torus


    %print(['testann-2014-11-20-multi-t2-g2nb' num2str(picInd) '.png'], '-dpng')
    % g2:no torus, move one disk at time

    % updated energyfunction
    %print(['testann-2014-12-05-multi-1-energy-b' num2str(picInd) '.png'], '-dpng')
    % refactor test
    print(['testann-2015-01-28-test-1-' num2str(picInd) '.png'], '-dpng')
end
