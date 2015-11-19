% test run: basic version of annealing
% (fine level of detail, each state stored)
% runannealingbasicf_small with a bit faster schedule

datapics_mat = 'testdata-shared/testdatapics_small.mat'
basename = 'basicf_small_t96'

% set up annSettings struct
annSettings.ensembleSize = 100;

annSettings.temperature = @(told) basictemperature(told, 0.96); % 0.96 instead of 0.98
annSettings.transition  = @(x,y,r,N,M) basictransition(x,y,r,N,M, max(M/15, N/15));
annSettings.cost        = @(x,y,r,data) basiccost(x,y,r,data,0,1);

runannealing(datapics_mat, basename, annSettings, 1);
