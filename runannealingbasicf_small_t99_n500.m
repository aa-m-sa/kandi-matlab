% test run: basic version of annealing
% (fine level of detail, each state stored)
% runannealingf_small with a longer schedule (n = 500 instead of 300)

datapics_mat = 'testdata-shared/testdatapics_small.mat'
% name of this scenario
basename = 'basicf_small_t99_n500'
% set up annSettings struct
annSettings.ensembleSize = 100;
annSettings.temperature = @(told) basictemperature(told, 0.99);
annSettings.transition  = @(x,y,r,N,M) basictransition(x,y,r,N,M, max(M/15, N/15));
annSettings.cost        = @(x,y,r,data) basiccost(x,y,r,data,0,1);
annSettings.temp_n      = 500;

runannealing(datapics_mat, basename, annSettings, 1);
