% run annealing on datasets 2_*

datapics1 = 'testdata-shared/testdata2_1.mat'
datapics2 = 'testdata-shared/testdata2_2.mat'
datapics3 = 'testdata-shared/testdata2_3.mat'
datapics4 = 'testdata-shared/testdata2_4.mat'
datapics5 = 'testdata-shared/testdata2_5.mat'

annSettings_core.ensembleSize = 100
annSettings_core.transition  = @(x,y,r,N,M) basictransition(x,y,r,N,M, max(M/15, N/15));
annSettings_core.cost        = @(x,y,r,data) basiccost(x,y,r,data,0,1);


annSettings_t99_n500 = annSettings_core;
annSettings_t99_n500.temp_n      = 500;
annSettings_t99_n500.temperature = @(told) basictemperature(told, 0.99);

set2runner(annSettings_t99_n500, 'set2-50x50-t99-n500')


annSettings_t98_n500 = annSettings_core;
annSettings_t98_n500.temp_n      = 500;
annSettings_t98_n500.temperature = @(told) basictemperature(told, 0.98);

set2runner(annSettings_t98_n500, 'set2-50x50-t98-n500')


annSettings_t96_n300 = annSettings_core;
annSettings_t96_n300.temp_n      = 300;
annSettings_t96_n300.temperature = @(told) basictemperature(told, 0.96);

set2runner(annSettings_t96_n300, 'set2-50x50-t96-n300')

annSettings_t94_n300 = annSettings_core;
annSettings_t94_n300.temp_n      = 300;
annSettings_t94_n300.temperature = @(told) basictemperature(told, 0.94);

set2runner(annSettings_t94_n300, 'set2-50x50-t94-n300')

annSettings_t90_n300 = annSettings_core;
annSettings_t90_n300.temp_n      = 300;
annSettings_t90_n300.temperature = @(told) basictemperature(told, 0.90);

set2runner(annSettings_t90_n300, 'set2-50x50-t90-n300')

function set2runner(annSettings, basename)
    % run annSettings on all 5 datapics (sub)sets from dataset 2

    runannealing(datapics1, [basename, '-c1-'], annSettings, 1);
    runannealing(datapics2, [basename, '-c2-'], annSettings, 1);
    runannealing(datapics3, [basename, '-c3-'], annSettings, 1);
    runannealing(datapics4, [basename, '-c4-'], annSettings, 1);
    runannealing(datapics5, [basename, '-c5-'], annSettings, 1);

end
