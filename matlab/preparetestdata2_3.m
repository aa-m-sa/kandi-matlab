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

prepare(picSets, N, ['testdata-shared/', datasetname, '.mat'], ['testdata-images/', datasetname,'-pic-'], 1)

