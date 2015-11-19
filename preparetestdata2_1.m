% create test data images

% stored in the folder testdata-shared

% image size
N = 50;

datasetname = 'testdata2_1'

picSets = {};
% params for test pics
radii_series_1 = 2.^(1:0.5:5)
rn1 = length(radii_series_1);
% first set: 1 circle
for p = 1:rn1
    picSets{p} = [25 25 radii_series_1(p)]
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

