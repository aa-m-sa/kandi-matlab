% run annealing on datasets 2_*

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

