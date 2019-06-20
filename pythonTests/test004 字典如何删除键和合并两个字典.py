#coding:UTF-8
#__autor__='wyxces'

'''
4、字典如何删除键和合并两个字典
del和update方法
'''

#定义字典
mydict = {"pb_ln_cons_atv_maxpct" : 0.26,
		    "pb_ln_morg_dftmons" : -99,
		    "pb_ln_busi_amt_lst" : -99,
		    "pb_ln_car_maxdftmons_2y" : -99,
		    "pb_ln_all_atv_maxdays" : 614,
		    "pb_ln_morg_atv_bal" : -99,
		    "pb_ln_all_maxnpfmmons_1y" : 0,
		    "pb_cd_curt_dft_minmon" : -99,
		    "pb_acd_dft_mons" : -99,
		    "pb_cd_uncc_maxlmt" : -99}
print('原字典信息为：\n\t',mydict)

#删除键
del mydict['pb_cd_uncc_maxlmt']
print('删除pb_cd_uncc_maxlmt后的字典信息为：\n\t',mydict)

#合并两个字典
mydict2 = {"pb_sf_qry_6m" : 1,
		    "pb_org_qry_loan_1m" : 0,
		    "pb_ln_car_ct_new3m" : -99,
		    "pb_ln_cons_npfm_ct_2y" : 0}
print('第二个字典的信息为：\n\t', mydict2)
mydict.update(mydict2)
print('mydict与mydict2合并后的字典信息为：\n\t',mydict)

