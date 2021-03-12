# -*- coding:utf-8 -*-

import streamlit as st
from PIL import Image
st.set_page_config('演算动态列线图',page_icon='random')

title='''<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">演算动态列线图</h2>
</div>'''
st.write(title, unsafe_allow_html=True)

st.write('### ')
st.info('Welcome:heart:! 在医学研究领域,有许多的列线图不断被制作出来,发布在pubmed、知网等数据库中，期望为临床决策提供经验指导，但是由于种种原因，这些研究成果并没有被人认识和利用，静态列线图使用不便是其中原因之一，为此我们通过论文发表的数据推导公式而制作出动态的列线图，为了区别通过数据获得的传统动态列线图，我称之为“演算动态列线图”。这里是一个关于发布演算动态列线图的网站，所有的列线图是根据论文公布的公式或者数据经过演算制作而成,与传统的动态列线图的制作方式有区别,预测准确度上与论文公布列线图没有区别,但形式上更灵活,使用更简便，后期会制作动态列线图的手机APP版本，敬请期待!联系方式:liuyp2080@163.com。')

st.write('请选择感兴趣的板块:')
col1,col2,col3,col4=st.beta_columns(4)
col5,col6,col7,col8=st.beta_columns(4)
select1=col1.checkbox('动态列线图-成人肿瘤')
select2=col2.checkbox('动态列线图-慢性疾病')
select3=col3.checkbox('动态列线图-妇科')
select4=col4.checkbox('动态列线图-儿科',value=True)
select5=col5.checkbox('动态列线图-重症')
if select1:

    import streamlit as st
    from PIL import Image
    import numpy as np

    def toweight(ls_hr):
        list_weight = list(map(np.log, ls_hr))
        return list_weight

    st.header('1、甲状腺微小瘤转移概率预测计算器')
    thyroid_nomo = Image.open('thyriod_nom.png')
    st.image(thyroid_nomo, width=400)
    st.info('参考文献:杨瑞,张守鹏,黄韬,明洁,杨鹏,朱俊玲,瞿芳.cN0期甲状腺微小乳头状癌淋巴结转移模型的构建和验证\n'
            '以及手术方式探讨[J].临床耳鼻咽喉头颈外科杂志,2021,35(02):137-140.说明:根据文献介绍，该研究纳入病例670例，预测概率值的阈值为0.55时,中央组淋巴结转移\n'
            '预测的准确率为68.5%。')
    st.sidebar.subheader('1、甲状腺微小瘤转移概率预测')
    para_size = st.sidebar.slider('肿瘤直径', min_value=1.0, max_value=10.0, step=0.1)
    col1, col2, col3 = st.beta_columns(3)
    col1.write('您选择的肿瘤直径是：{}mm'.format(para_size))
    age_select = st.sidebar.radio('性别', ['女', '男'], )
    col2.write('您选择的性别是：{}性'.format(age_select))
    if age_select == '女':
        para_sex = 0
    else:
        para_sex = 1
    para_age = st.sidebar.slider('患者年龄', 10, 75)
    col3.write('您选择的患者年龄是：{}岁'.format(para_age))

    list_para = [para_size, para_sex, para_age]
    list_or = [1.26579, 2.50828, 0.94866]
    betaZero = 0.0665
    # formula logic regression
    list_weight = toweight(list_or)
    multiply_list = [a * b for a, b in zip(list_weight, list_para)]
    z = sum(multiply_list) + betaZero
    q = 1 + np.exp(-z)
    prob = 1 / q

    st.success(r'该患者甲状腺微小肿瘤的发生淋巴结转移概率为{:.2f}%:'.format(prob * 100))
#___________________________________________________________________________________
    st.header('2、甲状腺癌侧颈部淋巴节转移概率计算器')
    thyroid_llnm = Image.open('thyroid_llnm_nomo.png')
    st.image(thyroid_llnm, width=400)
    st.info('参考文献:周瑾,周世崇,李佳伟,王宇,陈雅玲,王芬,智文祥,陈敏,常才.单发甲状腺乳头状癌侧颈部淋巴结转移的相关因素分析[J].中华超声影像学杂志,2019(11):971-972-973-974-975.说明:'
            )
    st.sidebar.subheader('2、甲状腺癌侧颈部淋巴节转移概率预测')
    col1, col2, col3, col4 = st.beta_columns(4)
    CLNM_select = st.sidebar.radio('中央淋巴结转移', ['无', '有'], )
    col1.write('中央淋巴结转移为：{}'.format(CLNM_select))
    if CLNM_select == '无':
        CLNM = 0
    else:
        CLNM = 1
    size_select = st.sidebar.radio('病灶最大直径为', ['≤10mm', '<10mm且≤20mm','>20mm'], )
    col2.write('病灶最大直径为：{}'.format(size_select))
    if size_select =='≤10mm':
        size_15=0
        size_20=0
    elif size_select=='<10mm且≤20mm':
        size_15 = 1
        size_20 = 0
    else:
        size_15 = 0
        size_20 = 1
    pos_select = st.sidebar.radio('位置', ['峡部', '上部','中部','下部','多部位'], )
    col3.write('位置为：{}'.format(pos_select))
    if pos_select =='峡部':
        pos_up=0
        pos_middle=0
        pos_down=0
        pos_all=0
    elif pos_select=='上部':
        pos_up = 1
        pos_middle = 0
        pos_down = 0
        pos_all = 0
    elif pos_select=='中部':
        pos_up = 0
        pos_middle = 1
        pos_down = 0
        pos_all = 0
    elif pos_select=='下部':
        pos_up = 0
        pos_middle = 0
        pos_down = 1
        pos_all = 0
    else:
        pos_up = 0
        pos_middle = 0
        pos_down = 0
        pos_all = 1
    microcalcification_select = st.sidebar.radio('微钙化', ['否', '是'], )
    col4.write('微钙化为：{}'.format(microcalcification_select))
    if microcalcification_select == '否':
        microcali= 0
    else:
        microcali = 1
    list_para = [CLNM,size_15,size_20,pos_up,pos_middle,pos_down,pos_all,microcali]
    list_or = [14.871,2.071,2.262,9.784,5.595,3.001,23.345,1.548]
    betaZero =-6.31342
    # formula logic regression
    list_weight = toweight(list_or)
    multiply_list = [a * b for a, b in zip(list_weight, list_para)]
    z = sum(multiply_list) + betaZero
    q = 1 + np.exp(-z)
    prob = 1 / q

    st.success(r'该患者侧颈部淋巴结转移的概率为{:.2f}%:'.format(prob * 100))

    # __________________________________________________________________________
    st.header('3、甲状腺术后低钙风险预测计算器')
    thyroid_hypocalcemia = Image.open('hypocalcemia.png')
    st.image(thyroid_hypocalcemia, width=400)
    st.info('参考文献:李岚,刘畅,肖明.预测甲状腺术后发生低钙血症的风险列线图模型建立[J].重庆医学,2021,50(03):461-465.说明:'
            )
    st.sidebar.subheader('3、甲状腺术后低钙风险预测')
    malignant_select = st.sidebar.radio('恶性肿瘤', ['否', '是'], )
    col1, col2, col3, col4, col5, col6 = st.beta_columns(6)
    col1.write('恶性肿瘤为：{}'.format(malignant_select))
    bilateral_select = st.sidebar.radio('双侧病变', ['否', '是'], )
    col2.write('双侧病变为：{}'.format(bilateral_select))
    central_node_select = st.sidebar.radio('清扫中央组淋巴结', ['否', '是'], )
    col3.write('清扫中央组淋巴结为：{}'.format(central_node_select))
    posterior_capsule_select = st.sidebar.radio('甲状腺后被膜破坏', ['否', '是'], )
    col4.write('甲状腺后被膜破坏为：{}'.format(posterior_capsule_select))
    operation_time_select = st.sidebar.radio('手术时间超过100分钟', ['否', '是'], )
    col5.write('手术时间超过100分钟为：{}'.format(operation_time_select))
    parathyroidectomy_select = st.sidebar.radio('甲状旁腺切除', ['否', '是'], )
    col6.write('甲状旁腺切除为：{}'.format(parathyroidectomy_select))

    paras = []
    for i in [malignant_select, bilateral_select, central_node_select, posterior_capsule_select, operation_time_select,
              parathyroidectomy_select]:
        if i == '否':
            para = 0
        else:
            para = 1
        paras.append(para)
    list_para = paras
    list_or = [2.546, 3.204, 2.582, 3.508, 3.658, 2.553]
    betaZero = -4.668
    # formula logic regression
    list_weight = toweight(list_or)
    multiply_list = [a * b for a, b in zip(list_weight, list_para)]
    z = sum(multiply_list) + betaZero
    q = 1 + np.exp(-z)
    prob = 1 / q

    st.success(r'该患者甲状腺术后发生低钙血症概率为{:.2f}%:'.format(prob * 100))

#____________________________________________________________________________________
    st.header('3、甲状腺癌患者术后出血风险预测计算器')
    thyroid_bloody = Image.open('bloody.png')
    st.image(thyroid_bloody, width=400)
    st.info('参考文献:郑艳,张茜,孙菲.个人化预测甲状腺癌患者术后出血风险的列线图模型的建立[J].医学综述,2021,27(03):609-613.说明:'
            )
    st.sidebar.subheader('3、甲状腺癌患者术后出血风险预测')
    hypertension_select = st.sidebar.radio('合并高血压', ['否', '是'], )
    col1, col2, col3,col4,col5,col6 = st.beta_columns(6)
    col1.write('合并高血压为：{}'.format(hypertension_select))
    fullcut_select = st.sidebar.radio('甲状腺全切', ['否', '是'], )
    col2.write('甲状腺全切为：{}'.format(fullcut_select))
    tumor_stage_select = st.sidebar.radio('肿瘤分期达III期', ['否', '是'], )
    col3.write('肿瘤分期达III期为：{}'.format(tumor_stage_select))
    tumor_size_select = st.sidebar.radio('肿瘤尺寸达4cm', ['否', '是'], )
    col4.write('肿瘤尺寸达4cm为：{}'.format(tumor_size_select))
    nerve_invasion_select = st.sidebar.radio('喉返神经浸润', ['否', '是'], )
    col5.write('喉返神经浸润为：{}'.format(nerve_invasion_select))
    node_metastasis_select = st.sidebar.radio('淋巴结转移', ['否', '是'], )
    col6.write('淋巴结转移为：{}'.format(node_metastasis_select))

    paras=[]
    for i in [hypertension_select,fullcut_select,tumor_stage_select,tumor_size_select,nerve_invasion_select,node_metastasis_select]:
        if i == '否':
            para = 0
        else:
            para = 1
        paras.append(para)
    list_para=paras
    list_or = [12.33,6.12,4.137,5.118,16.477,5.296]
    betaZero = -5.256
    # formula logic regression
    list_weight = toweight(list_or)
    multiply_list = [a * b for a, b in zip(list_weight, list_para)]
    z = sum(multiply_list) + betaZero
    q = 1 + np.exp(-z)
    prob = 1 / q

    st.success(r'该患者甲状腺术后出血的风险为{:.2f}%:'.format(prob * 100))
 #___________________________________________________________________________


    #________________________________________________________________________
    st.header('4、四肢骨肉瘤生存率预测计算器')
    bone_tumor = Image.open('bone_tumor.jpg')
    st.image(bone_tumor, width=400)
    st.info('参考文献：来源于柳昌全,赵广雷,陈康明,王思群,魏亦兵,黄钢勇,陈杰,石晶晟,夏军,陈飞雁.基于SEER数据库的四肢骨肉瘤预后相关列线图的\n'
            '构建[J].中国骨与关节杂志,2020,9(08):563-571.说明：所有四肢骨肉瘤患者的数据来源于SEER 数据库 (1995年至2014年)；\n'
            '组织学类型是骨肉瘤 ( 9180-普通型骨肉瘤，9181-软骨母细胞性骨肉瘤，9182-纤维母细胞性骨肉瘤，9183-血管扩张性骨肉瘤，9184-paget’s 骨肉瘤，9185-小细胞骨肉瘤，9186-中心性骨肉\n'
            '瘤，9187-骨内高分化骨肉瘤，9192-骨旁骨肉瘤，9193-骨膜骨肉瘤，9194-高等级骨表面骨肉瘤。')
    st.sidebar.subheader('4、四肢骨肉瘤生存率预测')
    age_select = st.sidebar.radio('患者年龄分层', ['<21', '21~46', '>=46'])
    if age_select == '<21':
        para_age_1 = 0
        para_age_2 = 0
    elif age_select == '21~46':
        para_age_1 = 1
        para_age_2 = 0
    else:
        para_age_1 = 0
        para_age_2 = 1
    col1, col2, col3, col4, col5 = st.beta_columns(5)
    col1.write('您所选择的年龄是:{}'.format(age_select))
    period_select = st.sidebar.radio('肿瘤分期', ['局部性', '区域性', '远处转移'])
    if period_select == '局部性':
        para_period_1 = 0
        para_period_2 = 0
    elif period_select == '区域性':
        para_period_1 = 1
        para_period_2 = 0
    else:
        para_period_1 = 0
        para_period_2 = 1
    col2.write('您所选择的肿瘤分期是:{}'.format(period_select))
    operation = st.sidebar.radio('手术与否', ['是', '否'])
    if operation == '是':
        para_operation = 0
    else:
        para_operation = 1
    col3.write('您所选择的手术情况是:{}'.format(operation))
    size = st.sidebar.radio('肿瘤尺寸', ['<13.9', '>=13.9'])
    if size == "<13.9":
        para_size = 0
    else:
        para_size = 1
    col4.write('您所选择的肿瘤尺寸是:{}'.format(size))
    type = st.sidebar.selectbox('病理类型', ['9192', '9182', '9186', '9183', '9180', '9181'])
    if type == '9192':
        para_type_1 = 0
        para_type_2 = 0
        para_type_3 = 0
        para_type_4 = 0
        para_type_5 = 0
    elif type == '9181':
        para_type_1 = 1
        para_type_2 = 0
        para_type_3 = 0
        para_type_4 = 0
        para_type_5 = 0
    elif type == '9180':
        para_type_1 = 0
        para_type_2 = 1
        para_type_3 = 0
        para_type_4 = 0
        para_type_5 = 0
    elif type == '9183':
        para_type_1 = 0
        para_type_2 = 0
        para_type_3 = 1
        para_type_4 = 0
        para_type_5 = 0
    elif type == '9186':
        para_type_1 = 0
        para_type_2 = 0
        para_type_3 = 0
        para_type_4 = 1
        para_type_5 = 0
    else:
        para_type_1 = 0
        para_type_2 = 0
        para_type_3 = 0
        para_type_4 = 0
        para_type_5 = 1
    col5.write('您所选择的肿瘤病理类型是:{}'.format(type))

    def toweight(ls):
        list_weight = list(map(np.log, ls))
        return list_weight

    # output
    basic_rate_adopt_1 = 0.9883522937528895
    basic_rate_adopt_3 = 0.9409661226740611
    basic_rate_adopt_5 = 0.9175902823690558
    hr = [1.63, 3.88, 1.31, 3.50, 2.10, 1.40, 2.635, 2.464, 2.151, 1.719, 1.161]
    list_para = [para_age_1, para_age_2, para_period_1, para_period_2, para_operation, para_size, para_type_1,
                 para_type_2, para_type_3, para_type_4, para_type_5]
    list_weight = toweight(hr)
    var = [a * b for a, b in zip(list_weight, list_para)]
    survival_rate_1year = basic_rate_adopt_1 ** np.exp(sum(var))
    survival_rate_3year = basic_rate_adopt_3 ** np.exp(sum(var))
    survival_rate_5year = basic_rate_adopt_5 ** np.exp(sum(var))
    st.success('该患者的1年生存率为{:.2f}%，3年生存率为{:.2f}%，5年生存率为{:.2f}%。'.format(survival_rate_1year * 100, survival_rate_3year * 100,survival_rate_5year * 100))

if select2:
    st.write('建设中,敬请期待')
if select3:
    st.write('建设中,敬请期待')
if select4:
    import streamlit as st
    from PIL import Image
    import numpy as np

    def toweight(ls_hr):
        list_weight = list(map(np.log, ls_hr))
        return list_weight
    st.header('1、Refractory Mycoplasma Pneumoniae Pneumonia in Children')
    thyroid_nomo = Image.open('mycoplasma_pneumoniae.png')
    st.image(thyroid_nomo, width=400)
    st.info('参考文献:Cheng S, Lin J, Zheng X, Yan L, Zhang Y, Zeng Q, Tian D, Fu Z, Dai J. Development and validation of a simple-to-use nomogram for predicting refractory Mycoplasma pneumoniae pneumonia in children. Pediatr Pulmonol. 2020 Apr;55(4):968-974. doi: 10.1002/ppul.24684. Epub 2020 Feb 10. PMID: 32040888.说明:用论文公布OR制作而成(与公式相比有一个值有出入(Albumin计算为-0.139,而公式中为-0.135))。')
    st.sidebar.subheader('1、Refractory Mycoplasma Pneumoniae Pneumonia in Children')
    para_LDH = st.sidebar.slider('Lactate Dehydrogenase', min_value=0, max_value=1600, step=10)
    col1, col2, col3,col4 = st.beta_columns(4)
    col1.write('Lactate Dehydrogenase：{}U/L'.format(para_LDH))
    para_albumin = st.sidebar.slider('Albumin', min_value=10, max_value=55, step=1)
    col2.write('Albumin：{}g/L'.format(para_albumin))
    para_neutrophil= st.sidebar.slider('Neutrophil Ratio', min_value=0.2, max_value=0.9, step=0.01)
    col3.write('Neutrophil Ratio：{}'.format(para_neutrophil))
    highfever_select = st.sidebar.radio('High Fever', ['No', 'Yes'], )
    col4.write('High fever：{}'.format(highfever_select))
    if  highfever_select == 'No':
        para_highfever = 0
    else:
        para_highfever = 1

    list_para = [para_LDH,para_albumin, para_neutrophil, para_highfever]
    list_or = [1.004,0.87,1160,5.54]
    betaZero = -3.5
    # formula logic regression
    list_weight = toweight(list_or)
    multiply_list = [a * b for a, b in zip(list_weight, list_para)]
    z = sum(multiply_list) + betaZero
    q = 1 + np.exp(-z)
    prob = 1 / q

    st.success(r'结果：该患者患Mycoplasma pneumoniae肺炎概率为{:.2f}%:'.format(prob * 100))
    # __________________
    st.header('2、Survival in Children Newly Diagnosed with High-risk Neuroblastoma')
    bone_tumor = Image.open('high_risk_neuroblastoma.png')
    st.image(bone_tumor, width=400)
    st.info('参考文献：Moreno L, Guo D, Irwin MS, Berthold F, Hogarty M, Kamijo T, Morgenstern D, Pasqualini C, Ash S, Potschger U, Ladenstein R, Valteau-Couanet D, Cohn SL, Pearson ADJ, London WB. A nomogram of clinical and biologic factors to predict survival in children newly diagnosed with high-risk neuroblastoma: An International Neuroblastoma Risk Group project. Pediatr Blood Cancer. 2021 Mar;68(3):e28794. doi: 10.1002/pbc.28794. Epub 2020 Nov 18. PMID: 33205902.')
    st.sidebar.subheader('2、Survival in Children Newly Diagnosed with High-risk Neuroblastoma')
    mycn_select = st.sidebar.radio('MYCN Status', ['NotAmp', 'Unknown', 'Amp'])
    if mycn_select == 'NotAmp':
        para_mycn_1 = 0
        para_mycn_2 = 0
    elif mycn_select == 'Unknown':
        para_mycn_1 = 1
        para_mycn_2 = 0
    else:
        para_mycn_1 = 0
        para_mycn_2 = 1
    col1, col2, col3 = st.beta_columns(3)
    col1.write('MYCN Status:{}'.format(mycn_select))
    para_ldh=st.sidebar.slider("LDH(U/L)",min_value=0,max_value=24000,step=100)
    col2.write("LDH:{}U/L".format(para_ldh))

    bone_metastasis_select = st.sidebar.radio('Bone Marrow Metastasis', ['Absence', 'Unknown', 'Presence'])
    if bone_metastasis_select == 'Absence':
        para_bone_metastasis_1 = 0
        para_bone_metastasis_2 = 0
    elif bone_metastasis_select == 'Uknown':
        para_bone_metastasis_1 = 1
        para_bone_metastasis_2 = 0
    else:
        para_bone_metastasis_1 = 0
        para_bone_metastasis_2 = 1
    col3.write('Bone Merrow metastasis:{}'.format(bone_metastasis_select))

    def toweight(ls):
        list_weight = list(map(np.log, ls))
        return list_weight


    # output

    basic_rate_adopt_3 = 0.73710233

    hr = [1.2,1.5,1.00005,1.7,2.1]
    list_para = [para_mycn_1,para_mycn_2,para_ldh,para_bone_metastasis_1,para_bone_metastasis_2]
    list_weight = toweight(hr)
    var = [a * b for a, b in zip(list_weight, list_para)]
    survival_rate_3year = basic_rate_adopt_3 ** np.exp(sum(var))

    st.success(
        '该患者的3年生存率为{:.2f}%'.format(survival_rate_3year * 100))

    # ___________________
if select5:
    st.write('建设中,敬请期待')
