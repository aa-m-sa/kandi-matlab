% create test data images

% stored in the folder testdata-shared

% image size
N = 50;

datasetname = 'testdata2_3'

picSets = {};
% params for test pics

radii_series_2 = 2.^(1:1:4)
rn2 = length(radii_series_2);

% 3 circles, one stays constant
for p1 = 1:1:rn2
    for p2 = 1:1:rn2
        picSets{(p1-1)*rn2 + p2} = [16 16 12; 15 35 radii_series_2(p1); 40 20 radii_series_2(p2)]
    end
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

