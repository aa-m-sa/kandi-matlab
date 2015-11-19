% create test data images

% stored in the folder testdata-shared

% image size
N = 50;

datasetname = 'testdata2_4'

picSets = {};
% params for test pics

radii_series_2 = 2.^(1:1:4)
rn2 = length(radii_series_2);

% 4 circles, one of them changes

for p1 = 1:1:rn2
    picSets{p1} = [16 44 10; 44 44 8; 44 16 10; 18 18 radii_series_2(p1)];
end

numPics = length(picSets)

nDataCircles = zeros(1, numPics);

dataSets = {};

for picInd = 1:numPics
    fighandle = figure('visible', 'off')
    %fighandle = figure()
    clf;
    picSet = picSets(picInd);
    picSet = picSet{:}
    nDataCircles(picInd) = length(picSet(:, 1));
    x = picSet(:, 1);
    y = picSet(:, 2);
    r = picSet(:, 3);

    A_data = createdataimage(x, y, r, N, N);
    imagesc(A_data)
    colormap(gray)
    axis image
    dataSets{picInd} = A_data;

    print(fighandle, ['testdata-images/' datasetname '-pic-' num2str(picInd) '.png'], '-dpng')
end

save(['testdata-shared/' datasetname '.mat'], 'dataSets', 'numPics', 'nDataCircles');

