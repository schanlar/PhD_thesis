import numpy as np
import matplotlib.pyplot as plt

plt.style.use(['default', 'science'])

ax = plt.gca()

# Hide X and Y axes label marks
ax.xaxis.set_tick_params(labelbottom=False)
ax.yaxis.set_tick_params(labelleft=False)

# Hide X and Y axes tick marks
ax.set_xticks([])
ax.set_yticks([])


hadronic = np.linspace(0,50)
hadronic_y = lambda x: x**2

quark = np.linspace(100, 150)
quark_y = lambda x: 100*x - 7500 

ax.plot(hadronic, hadronic_y(hadronic), c='k')
# ax.axhline(hadronic_y(hadronic[-1]), ls='--', c='grey')
# ax.axvline(hadronic[-1], ls='--', c='grey')
ax.plot(quark, quark_y(quark), c='k')

ax.plot([hadronic[-1], quark[0]], [hadronic_y(hadronic[-1]), quark_y(quark[0])], ls='--', c='k', label='Maxwell construction')
ax.plot([hadronic[-10], quark[10]], [hadronic_y(hadronic[-10]), quark_y(quark[10])], ls='-.', c='k', label='Gibbs construction')
ax.plot([hadronic[-1], hadronic[-1]], [hadronic_y(hadronic[-1]), 0], ls=':', c='grey')
ax.plot([quark[0], quark[0]], [quark_y(quark[0]), 0], ls=':', c='grey')
ax.plot([0, hadronic[-1]], [hadronic_y(hadronic[-1]), hadronic_y(hadronic[-1])], ls=':', c='grey')


ax.legend(frameon=False)

ax.set_xlabel(r'$\varepsilon$ [arb. unit]')
ax.set_ylabel(r'$P$ [arb. unit]')
ax.set_xlim(0, 155)
ax.set_ylim(0, 10000)
plt.text(10, 1000, s='HP')
plt.text(130, 4500, s='QP')
plt.text(52, 650, s=r'$\varepsilon_c$')
plt.text(102, 650, s=r'$\varepsilon_c + \Delta \varepsilon$')
plt.text(20, 2750, s=r'$P_c$')

plt.show()
# plt.savefig("/Users/schanlar/Desktop/p_vs_epsilon.png", dpi=300, bbox_inches='tight')
