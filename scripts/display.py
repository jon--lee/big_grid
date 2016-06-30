import numpy as np
from analysis import Analysis
ITER = 40
rewards = None
sinks = None
data_directory = 'comparisons/boost_4dim_dt_full_data/'
comparisons_directory = 'comparisons/boost_4dim_dt_full_comparison/'


value_iter_data = np.load(data_directory + '4dim_boost_dt_full_sup_data.npy')
classic_il_data = np.load(data_directory + '4dim_boost_dt_full_classic_il_data.npy')
dagger_data = np.load(data_directory + '4dim_boost_dt_full_dagger_data.npy')

dagger_acc = np.load(data_directory + '4dim_boost_dt_full_dagger_acc.npy')
classic_il_acc = np.load(data_directory + '4dim_boost_dt_full_classic_il_acc.npy')

analysis = Analysis(15, 15, ITER, rewards=rewards, sinks=sinks, desc="General reward comparison")

analysis.get_perf(value_iter_data)
analysis.get_perf(classic_il_data)
analysis.get_perf(dagger_data)
analysis.plot(names=['Value Iteration', 'DT IL', 'DT DAgger'], ylims=[0, 120])
        #filename=comparisons_directory+'boost_dim_dt_full_reward_comparison.png', ylims=[-60, 100])

acc_analysis = Analysis(15, 15, ITER, rewards = rewards, sinks=sinks, desc='Accuracy comparison')
acc_analysis.get_perf(classic_il_acc)
acc_analysis.get_perf(dagger_acc)
acc_analysis.plot(names = ['DT IL Acc.', 'DT DAgger Acc.'], label='Accuracy', ylims=[0, 1])
        #filename=comparisons_directory+'boost_4dim_dt_full_acc_comparison.png', ylims=[0,1])


