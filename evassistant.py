# %%
import numpy as np
class logistic:
    def __init__(self,ls_or,ls_xvar,intercept):
        self.ls_or=ls_or
        self.ls_xvar=ls_xvar
        self.intercept=intercept
    def prob(self):
        ls_beta=[np.log(x) for x in self.ls_or]
        ls_weight=[a*b for a,b in zip(ls_beta,self.ls_xvar)]
        z=sum(ls_weight)+self.intercept
        q=1+np.exp(-z)
        prob=1/q
        return prob
    def pi(self):
        ls_beta=[np.log(x) for x in self.ls_or]
        ls_weight=[a*b for a,b in zip(ls_beta,self.ls_xvar)]
        pi=sum(ls_weight)
        return pi

def intercept_estimate(prob,ls_xvar,ls_or):
    ls_beta=[np.log(x) for x in ls_or]
    ls_weight=[a*b for a,b in zip(ls_beta,ls_xvar)]
    var2=np.subtract(np.divide(1,prob),1)
    intercept = -np.log(var2)-sum(ls_weight)
    return intercept


class cox:
    def __init__(self,ls_hr,ls_xvar,basic_rate):
        self.ls_hr=ls_hr
        self.ls_xvar=ls_xvar
        self.basic_rate=basic_rate
    def survival_rate(self):
        ls_beta=[np.log(x) for x in self.ls_hr]
        ls_weight=[a*b for a,b in zip(ls_beta,self.ls_xvar)]
        pi=sum(ls_weight)
        survival_rate=self.basic_rate**np.exp(pi)
        return survival_rate
    def pi(self):
        ls_beta=[np.log(x) for x in self.ls_hr]
        ls_weight=[a*b for a,b in zip(ls_beta,self.ls_xvar)]
        pi=sum(ls_weight)
        return pi
def basic_rate_estimate(survival_rate,ls_xvar,ls_hr):
    ls_beta=[np.log(x) for x in self.ls_hr]
    ls_weight=[a*b for a,b in zip(ls_beta,ls_xvar)]
    var=np.exp(sum(ls_weight))    
    basic_rate=pow(survival_rate,1.0/var)
    return basic_rate 
#%%
if __name__=="__main__":
    basic_rate = 0.73710233
    ls_hr = [1.2,1.5,1.00005,1.7,2.1]
    ls_xvar = [1,2,3,4,5]
    model=cox(ls_hr,ls_xvar,basic_rate)
    print(model.survival_rate())
# %%

# %%
