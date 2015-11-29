
load('testdata-annealingbasic/ann-data-pic-7', 'enDataEnerg')
load('testdata-shared/testdatapics', 'dataSets')
load('testdata-annealingbasic/results-pic-7', 'enX', 'enY', 'enR')

finalEnergies = zeros(1, length(enDataEnerg));

for e = 1:length(enDataEnerg)
    energies = enDataEnerg{e};
    l = length(energies);
    finalEnergies(e) = energies(l);
end

% limits handpicked

binEdges = 2000:100:5000;
[binNums, binIdx] = histc(finalEnergies, binEdges);

figure()
hist(finalEnergies)

figure()
bar(binNums)

enXmat = cell2mat(enX)
enYmat = cell2mat(enY)
enRmat = cell2mat(enR)

% binIdx <= 5 = > doesn find the small circle
% <= 10 => some 'clustering' around it
% <= 15 -> quite clear cluster of read circles also in the general area of the
% small circle but lots of 'fail' circles (and we have used ensemble of the
% size 82)

binBestxs = enXmat(:, binIdx >= 3 & binIdx <=15);
binBestys = enYmat(:, binIdx >= 3 & binIdx <=15);
binBestrs = enRmat(:, binIdx >= 3 & binIdx <=15);

figure()
imshow(dataSets{7})
hold on;
for pick = 1:length(binBestxs)
    plotrescircles(binBestxs(:,pick), binBestys(:,pick), binBestrs(:,pick))
end
