import streamlit as st
from PIL import Image

# st.sidebar.checkbox('标准化')
# st.sidebar.checkbox('预测模型')
# st.sidebar.checkbox('观点')
st.balloons()
title='''<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">临床研究Collection</h2>
</div>'''
st.write(title,unsafe_allow_html=True)
# image=Image.open('test.jpg')
# st.image(image,caption='test', use_column_width=True)
st.write('### ')
st.info('Welcome! 这里是一个临床科研相关知识的网站，希望您能有所收获! ')

select=st.selectbox('请选择感兴趣的板块',['临床研究标准化','临床研究设计（观点）','临床预测模型（实践）'])

if select=='临床研究标准化':
    st.write('随着临床研究这个领域的不断发展和成熟，在前人的不断探索下，形成了许多经验，这些经验经过专家群体或者专业机构的总结、扩展成为\n'
        '业内人士普遍接受的行为准则，这里称为“标准化”。虽说在临床研究领域并没有强制要求一定要按照标准化的流程来进行, 然而尽可能地学习并\n'
        '遵守这些行为准则，有助于快速地且质量较高的开展自己的临床研究，避免可能产生的种种错误, 从而在短期内上手且产出较高质量的研究\n'
        '成果。如果说临床科研纷繁复杂，犹如险峻陡峭的华山，而”标准化”则是从事临床科研的一条捷径。')

    st.write('临床研究包含多个环节, 标准化是针对临床试验的每个环节来制定的。目前主要的标准化环节有：1、研究报告格式和内容的标准化，之所以要进行这方面的标准化是因为\n'
         '许多报告格式和内容不规范, 试验中许多重要的, 体现试验质量的参数没有被报告出来，导致读者无从判断试验结论的可靠性，所以对研\n'
         '究报告的格式和内容进行了规范; 2.临床研究数据库建设的标准化。数据库要求一方面安全的存储数据，另一方面便于数据的后续分析和交流，\n'
         '在临床数据和分析数据之间起到“承前启后”的作用，有助于更充分地管理和利用收集的数据，数据的交流和合并; 3.核心结局变量集。结局变量是\n'
         '临床试验中所要收集的三大类变量（预测变量、混杂变量和结局变量）之一，其标准化有助于各个临床试验之间进行相互地比较，也为后续的Meta\n'
         '分析奠定基础,规范结局变量的收集，避免变量收集过多或者收集不全的情况。')
    st.subheader("一、核心结局指标集")
    st.write("**简介**：在从事临床研究过程中的可以体会到，自己领域的系列研究以及同行的研究在收集结局变量方面往往有相似性。这是结局变量标准化的基础：\n"
         "同领域内的研究往往有相同的结局变量，而相同的结局变量也很可能会有相同的混杂变量。某些结局变量收集不齐全会直接导致试验结论不全面，与\n"
         "与同行的研究不可比(结局指标不同)。在这样的背景下，临床试验核心指标集（COS）应运而生，COS是某特定病证相关的所有临床研究都应测量\n"
         "和报告的、最少但最重要的指标集合，是由国际学术组织有效性试验核心结局指标测量（[COMET](www.comet-initiative.org/)）成立并提出倡议。\n"
         "该网站上建立了COS数据库，可以查询下载目前已经建立的各个研究领域的COS。需要指出的是，许多小的研究领域并没有现成的COS，需要自己进行创建，\n"
         "为此，该组织发布了COS的制定标准,指导COS的创建。2019年7月19日，中国循证医学\n"
        "中心和天津中医药大学循证医学中心共建的中国临床试验核心指标集研究中心在天津中医药大学新校区揭牌，标志着该项标准化工作受到国内专家的重视。")
    st.write('### --Collection--')
    st.info('[核心结局指标集COS文档](https://pan.baidu.com/s/1IYWHdoAZKkNOiW-v06AM5Q)（提取码-lcyj）')
    st.subheader('二、零成本建立中小型临床数据库')
    st.write("**简介：**建立临床数据库过程中涉及的两个标准化是“数据组织形式的标准化”和“变量名的标准化”。建立数据库肯定是为了长期的研究，较少是\n"
         "仅仅为了一个小课题，所以需要收集的数据可能比较多，包括某个疾病的方方面面，需要分门别类，每一类数据组成一张表格，多个表格之间以唯\n"
         "一的识别码进行关联，构建成所谓的关系型数据库；同一类的数据内部按照纵向数据结构或横向数据结构组织在同一张表格中。这里我们借鉴[CDISC](https://www.cdisc.org/)成型的\n"
         "方法构建我们自己的临床性数据库，避免了从头学习复杂的数据库构建的相关知识。“变量名的标准化”，也称为“公共数据元”，是在相似的研究中统一变量名称\n"
         "方便了后续的数据分析(编程)和数据之间的合并和交换。我们从实际经验中总结了零成本建立中小型数据库的方法，并将其发表在\n"
         "网络上，可以用关键词“零成本”“临床数据库”进行搜索阅读。")
    st.write('### --Collection--')
    st.success('[零成本建立中小型临床数据库资料](https://pan.baidu.com/s/1Qon9dAy_OTE7B54h8nlPPw)（提取码-lcyj）')
    st.subheader('三、试验结果报告的标准化')
    st.write("**简介：**这是由国际上科学家和编辑共同制定的一系列科研报告的规范，以提高临床研究报告的质量。这些规范包括《随机对照试验规范》\n"
         "（[CONSORT](http://www.consort-statement.org/)）、《观察性研究报告标准》（[STROBE](https://www.strobe-statement.org/index.php?id=strobe-home)）\n"
         "、《非随机对照试验报告规范》（[TREND](https://www.cdc.gov/trendstatement/)）和《诊断性研究标准》（STARD）。")
    st.write('### --Collection--')
    st.warning('[试验结果报告标准下载](https://pan.baidu.com/s/1sVbkHpq_oVsUtqCWP6slDA)（提取码-lcyj）')
    st.write("**------------------------------------------------------------------------------------------------------------**")
    st.write('--The End-- ')
elif select=='临床预测模型（实践）':
    st.write('临床预测模型的开发属于“医学检验研究设计”大类，其目标在于应用数学方法开发新的（复合的）检验从而改善临床决策，并非评价已有的检验。\n'
             '一个合格的临床研究预测模型，应该具备以下特点：1、研究对象应该与应用该规则的人群类似；2、应用了合适的数学方法构建模型，可选的方法包括\n'
             '逻辑回归、Cox风险比例模型、机器学习和深度学习；3、进行了充份的验证。医学数据往往是由标签的，属于“监督性学习”的范畴，Excel表格是存储数据的最常见形式。\n'
             '结合医学数据的一些特点我们在实践中也总结了一些经验，1、模型可操作性要强，体现在预测变量的数量不宜过多，有的研究宁可牺牲一些的预测准确度也要减少预测变量的数量；\n'
             '2、尝试用多种数学方法进行模型的构建或者采用集成或综合的方法来构建模型，特别是根据构建原理迥异的模型，比如决策树、神经网络、逻辑回归；\n'
             '然后从中选择较优的模型；3、样本量不宜过少，临床上的样本量通常不大，需要采用交叉验证\n'
             '或采用集成算法等数学方法进行一定程度的克服；4、对原始数据进行合适的处理等。下面以python语言编码粗略展示目前流行的非线性模型神经网络模型的构建流程。')
    st.write('* 数据处理')
    st.code('''
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical #分类变量one-hot编码
from tensorflow.keras.utils import normalize #连续变量标准化数据

iris=load_iris()
X_train, X_test, y_train, y_test=train_test_split(iris.data, iris.target, test_size = 0.2, random_state=0)
y_test=to_categorical(y_test)
y_train=to_categorical(y_train)
X_train=normalize(X_train)
X_test=normalize(X_test)
''')
    st.write('* 模型构建（带超参数调节）')
    st.code('''
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical #深度学习神经网络库

# nn structure
from keras.backend import clear_session
from keras.layers import Dense, Dropout
from keras.models import Sequential
from keras.optimizers import RMSprop
from keras.callbacks import ModelCheckpoint
from keras.callbacks import EarlyStopping
import optuna #超参数调节

def objective(trial):
    clear_session()
    # built 1 layer neural network
    model = Sequential()
    model.add(
        Dense(
            units=trial.suggest_categorical('units', [32, 64, 128]),
            activation=trial.suggest_categorical('activation', ['relu', 'linear']),
            input_shape=(X_train.shape[1],)))
    model.add(Dropout(rate=trial.suggest_uniform('drop_rate',0.0,1.0)))
    model.add(Dense(3, activation='softmax'))
    # We compile our model with a sampled learning rate.
    lr = trial.suggest_float("lr", 1e-5, 1e-1, log=True)
    model.compile(
        loss="binary_crossentropy", optimizer=RMSprop(lr=lr), metrics=["accuracy"]
    )
    callback_lists = [EarlyStopping(monitor="accuracy", patience=1),
                      ModelCheckpoint(filepath="my_model.h5", moniter="val_loss", save_best_only=True)]

    model.fit(
        X_train,
        y_train,
        validation_data=(X_test, y_test),
        shuffle=True,
        batch_size=trial.suggest_int('batch_size',1,50),
        epochs=500,
        verbose=False,
        callbacks=callback_lists
    )

    # Evaluate the model accuracy on the validation set.
    score = model.evaluate(X_test, y_test, verbose=0)
    return score[1]


if __name__ == "__main__":
    study = optuna.create_study(direction="maximize")
    study.optimize(objective, n_trials=100, timeout=600)

    print("Number of finished trials: {}".format(len(study.trials)))

    print("Best trial:")
    trial = study.best_trial

    print("  Value: {}".format(trial.value))
    print("  Params: ")

    for key, value in trial.params.items():
        print("    {}: {}".format(key, value))
''')
    st.write('* 模型评价')
    st.write('### --Collection--')
    st.write('[临床预测模型资料]()')
    st.write('*----------------------------------------------------------------------------------------------------------------*')
    st.write('--The End-- ')
else:
    st.write('### 一、不是所有的统计方法都需要了解')
    st.write('临床研究技能已经被列为一个临床医师的核心职业技能之一，从纷繁复杂的影响疾病因素中找出规律是医学进步的途径也是临床医生无可替代的责任。\n'
             '对于想从事临床研究的医生来说，当然是了解临床研究的知识愈多愈好，但是繁多而复杂的临床研究的知识常常使临床医生无从下手，甚至望而却步。')
    st.write('要解决这个问题，除了加强学习之外，临床医生要明确的一点就是，不是所有的临床研究的知识都需要了解。首先，根据研究目的，临床研究的知识可以\n'
             '分为因果关系的研究设计和医学检验的研究设计两大部分。一般临床科室（内科、外科等）的临床医生往往期望发现疾病相关因子（预测因素）与疾病结局\n'
             '（结局因素）之间的因果关系，就只需要了解因果关系的研究设计。这也是和这类医生的诊断疾病，去除病因等日常临床工作紧密相关的。另一方面，\n'
             '医学检验的研究设计是考察某一个因子是否适合用于预测疾病结局，它不强调两者之间是否具有因果关系，而是更加关注的是两者关系的精确性、准确性\n'
             '和特异性等等指标。这方面大家可以和检验科的工作进行类比，检验科的医生往往不关心检验指标和疾病之间是否存在因果关系，而只关心检验指标是不是\n'
             '能够反映疾病状况。其次，即使在因果关系的研究设计中，又可以细分为观察性研究设计和随机对照盲法的研究设计。后者多是用在临床药物试验的过程中，\n'
             '实施难度大，要求更多的人力和物力，需要有前期大量的动物实验和临床试验的结果作为前期工作，且与医生的日常工作距离较远，所以除非科室有较好的临床\n'
             '研究的条件或研究任务，也可暂时不做了解。')
    st.write('综上所述，在所有的临床研究的知识当中，一般临床医生需要（或是优先）了解的就是因果关系研究设计中的观察性\n'
             '研究设计的相关知识，罗列起来这些知识包括，横断面研究、病例对照研究、队列研究以及相关的统计方法——逻辑回归、线性回归和Cox回归。其它的临床研究的\n'
             '知识都可以作为进阶阶段的内容。')
    st.write('### 二、师兄和师弟的科研经历')
    st.write('教授在学习会上发表演说，强调作为临床医生要担当起一个医生不可推卸的临床科研的责任：发现临床问题，解决临床问题，致力于临床科研。\n'
             '然后，教授出了一个题目：X基因表观修饰水平(连续变量)和糖尿病（和并发症），并交代各位同学根据自己的实际情况设计课题。讲完就飘然离去。')
    st.write('王师兄是临床医学背景，是内分泌科的主治医师。平时在临床工作，接触糖尿病的患者，就设计了适合自己的试验方案：收集科室内糖尿病患者的血液\n'
             '并存储在医院样本库备用检测（准备检测X基因的表观修饰水平），进行随访观察患者糖尿病肾病等的并发症发生情况和可能的影响结局因素（混杂变量）\n'
             '，期望分析获得X基因的表观修饰水平与糖尿病肾病等并发症之间的因果联系。把采集样本的时间作为患者进入队列的时间，因为X基因的表观修饰水平可\n'
             '能受到糖尿病患病年限的影响，所以在结果分析中通过匹配“糖尿病患病年限”或多因素分析中纳入“糖尿病患病时间”进行处理。又因为队列中的患者会\n'
             '在不同的随访时间出现结局，所以通过采用多因素Cox分析得出最后的结果。试验设计的最后一步是估计样本量，通过咨询医院的循证医学中心的老师，\n'
             '王师兄确定了相关的参数：α=0.05，1-β=0.8，效应值（出现结局和未出现结局两组间X基因表观修饰水平的差值），X基因表观修饰水平测量的精确度\n'
             '（标准差），分析方法为t检验，并用PASS软件大概估计样本量。试验设计完成了，开始执行。结果因为没有考虑到结局出现需要较长的时间，导致用了\n'
             '很长的时间收集样本，完成试验的时间不得不延后，也延迟了毕业。王师兄不禁感叹如果科室里事先建立多任务糖尿病病例数据库，并且在样本库里储存\n'
             '了样本，就可以利用病例库来进行这个科研工作，就不会有完成延迟的情况。因为临床试验确认了X基因表观修饰水平是糖尿病某结局之间较强的因果联系，\n'
             '王师兄觉得可以在动物实验上进行验证并探讨其背后的机制，并以此撰写了国家自然科学基金标书来申请课题。')
    st.write('李师弟是检验科背景，不关注X基因表观修饰水平与糖尿病某并发症发生之间的因果关系，而是关注X基因表观修饰水平是否可以作为一个糖尿病某并发症的指标，\n'
             '选择了“诊断试验”的设计：收集门诊所有送到检验科的血样，检测X基因表观修饰水平，并收集患者的基本信息和是否被诊断为糖尿病某并发症的信息，\n'
             '数据分析计算灵敏度、特异度和似然比以及各自的置信区间。同样，李师弟也用PASS软件进行了样本量的计算。李师弟后来得到了阳性的结果，撰写了论文，\n'
             '后续进一步申请了专利，为临床提供新的诊断手段。')
    st.write('教授后来点评，虽然是出于同一个题目，两种设计的关注点不同，人群不同，分析方法不同，但是都符合两个人的背景知识，同样具有可行性。临床试验目前\n'
             '已经形成一定的规范和套路，一个临床医生不论什么学历，都可以学会临床试验的做法，获得这项必备的职业技能。另外，每个人背景不同，关注点不同，\n'
             '不是所有临床试验的方法都要去了解。希望各位在职的学生克服畏难的想法，积极掌握临床试验的规范。')
    st.write('### 三、论文呈现数据，图还是表？   ——绝对值数据用表，相对值数据用图')
    st.write('最近投稿的一篇文章，编辑部建议把行为学的图改成表格，到底是为什么呢？咱也不是科研新人，用图表示行为学的数据在多个杂志上也发表了文章数篇，\n'
             '比这家杂志水平高的也有。有心挣扎一下，但是另一句箴言浮现在心头“一切按照审稿人的意见!”，鉴于“是图还是表”也不是大是大非的问题，\n'
             '就遵照编辑部的意思将图改成了表，后来算是一切顺利。')
    st.write('那残留的那个问题，呈现数据，是图还是表？有没有标准答案呢。网络上广传的一个答案是，\n'
             '“根据数据或表达观点的需要选择最合适的表达形式。表格的优点是可以方便地列举大量精确数据或资料, 图形则可以直观、有效地表达复杂数据。因此,\n'
             ' 如果强调展示给读者精确的数值,就采用表格形式；如果要强调展示数据的分布特征或变化趋势, 则宜采用图示方法。”网上能广为流传，说明大家都接受这个\n'
             '答案。具体到我的问题是图还是表看来都可以，取决于偏好和目的：作者（我）是想直观地表达，所以用图，而编辑是想提供给读者精确的数据，所以用表。\n'
             '但是这里我还想提供一个我自己想出来的标准给大家参考。医学临床文章多采用表格，偏向于提供精确的数据，有时候整篇文章没有一个图；而医学基础研究多\n'
             '采用图，偏向于直观表述数据，有时候整篇文章没有一个表格。这是约定俗成，还是另有原因？')
    st.write('个人认为临床文章的数据多是绝对值，比如身高、体重或各种实验室\n'
             '检查数据等，其用表格提供这些绝对值的精确数据的最可能原因是为了后续的再分析，尤其是系统性综述中的meta分析，如果是提供图的话，meta分析的数据就无从摘录。\n'
             '反观基础研究除了个别的数据是绝对值数据（行为学数据或ELISA数据），多数数据是相对值数据，比如Western Blot的统计数据、免疫组化的半定量数据，\n'
             '且一般没有后续meta分析的步骤，所以一般是用图展示给读者形象的数据和趋势。然而，近年来，动物实验也开始提倡进行系统性综述，以便得出综合性的结论，\n'
             '医学基础试验用表格提供精确的数据也有了一定的必要性。所以，这里个人在原有的图表选择标准的基础上，附带提出一个想法，就是“绝对值数据用表，\n'
             '相对值数据用图”，供大家讨论。当大家在撰写一些临床与基础相结合的文章时候，这个标准或许能解决一些人在图表选择方面的困难。')
    st.write('### --Collection--')
    st.write('[临床研究设计学习资料]()')
    st.write('*----------------------------------------------------------------------------------------------------------------*')
    st.write('--The End-- ')