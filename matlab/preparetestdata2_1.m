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

prepare(picSets, N, ['testdata-shared/', datasetname, '.mat'], ['testdata-images/', datasetname,'-pic-'], 1)
