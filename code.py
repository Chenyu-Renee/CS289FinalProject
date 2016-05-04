a=list()
for i in range(105):
    a.append(i)
    
a.append(108)
a.append(107)
a.append(109)
a.append(110)
a.append(113)

ale=all_info.ix[:,a]

t=list()
for i in range(len(ale)):
    if all_info.ix[i,106]>10:
        t.append(1)
    if all_info.ix[i,106]<=10:
        t.append(0)

a=range(110)
a=a[5:]
al=ale.ix[:,a]


train=al

test=np.asarray(t)

train['user_count'][train['user_count'].isnull()]=np.mean(train['user_count'][train['user_count'].notnull()])

train['user_star'][train['user_star'].isnull()]=np.mean(train['user_star'][train['user_star'].notnull()])

train['user_useful'][train['user_useful'].isnull()]=np.mean(train['user_useful'][train['user_useful'].notnull()])

train_t=np.asarray(train)

a=random.sample(range(len(train_t)),150000)

b=list(set(range(len(train_t)))-set(a))

real_train=train_t[a,]
train_labels=test[a,]
vaild=train_t[b,]
valid_labels=test[b]

clf = RandomForestClassifier(n_estimators=10)

clf = clf.fit(real_train, train_labels)

ae=clf.predict(vaild)