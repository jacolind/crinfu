'''
analyze baskets using statsmodels

will be put somehwere else later. a file sjould not depend on the package but rather the anlaysis being made.
'''

import statsmodels.graphics.api as smg
import statsmodels.graphics.tsaplots as tsa

hie_data = sm.datasets.randhie.load_pandas()
retmat1
corr_matrix = np.corrcoef(retmat1.T)
corr_matrix.shape
smg.plot_corr(corr_matrix, cmap='viridis')

#tsa.plot_acf(x, ax=None, lags=None, alpha=0.05, use_vlines=True, unbiased=False, fft=False, title='Autocorrelation', zero=True, vlines_kwargs=None, **kwargs)

# plot
tsa.plot_acf(r1, lags=30, alpha=0.05, use_vlines=False)
plt.title('Autocorrelation ' + r1.name)
ylabel1 = 'corr of day t with day t minus lag'
xlabel1 = 'Lag'
plt.xlabel(xlabel1)
plt.ylabel(ylabel1)
plt.savefig('output/bsk/ret/ACF_bsk1.png')

# plot
tsa.plot_acf(ret_vcc_mat.BTC, use_vlines=False, lags=30, alpha=0.05)
plt.title('Autocorrelation BTC')
plt.xlabel(xlabel1)
plt.ylabel(ylabel1)
plt.savefig('output/bsk/ret/ACF_btc.png')

# todo: would be interesting to see this with intraday data