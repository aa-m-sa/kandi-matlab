function set2runner(annSettings, basename)
    % SET2RUNNER(annSettingsStruct, basename)
    % helper function for running annealing on dataset2
    % run annSettings on all 5 datapics (sub)sets from dataset 2
    datapics1 = 'testdata-shared/testdata2_1.mat'
    datapics2 = 'testdata-shared/testdata2_2.mat'
    datapics3 = 'testdata-shared/testdata2_3.mat'
    datapics4 = 'testdata-shared/testdata2_4.mat'
    datapics5 = 'testdata-shared/testdata2_5.mat'


    runannealing(datapics1, [basename, '-c1-'], annSettings, 1);
    runannealing(datapics2, [basename, '-c2-'], annSettings, 1);
    runannealing(datapics3, [basename, '-c3-'], annSettings, 1);
    runannealing(datapics4, [basename, '-c4-'], annSettings, 1);
    runannealing(datapics5, [basename, '-c5-'], annSettings, 1);

end
