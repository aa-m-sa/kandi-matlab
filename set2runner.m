function set2runner(annSettings, basename)
    % SET2RUNNER(annSettingsStruct, basename)
    % helper function for running annealing on dataset2
    % run annSettings on all 5 datapics (sub)sets from dataset 2

    runannealing(datapics1, [basename, '-c1-'], annSettings, 1);
    runannealing(datapics2, [basename, '-c2-'], annSettings, 1);
    runannealing(datapics3, [basename, '-c3-'], annSettings, 1);
    runannealing(datapics4, [basename, '-c4-'], annSettings, 1);
    runannealing(datapics5, [basename, '-c5-'], annSettings, 1);

end
