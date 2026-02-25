import re

content = open('slides/10-roc-auc.qmd').read()

import textwrap

# Replace Ex 1 part 1
part1_old = """:::: columns
:::: {.column width="50%"}
```{python}
#| echo: false
np.random.seed(4025)
probs = np.concatenate([np.random.uniform(0, 0.1, 100), np.random.uniform(0.9, 1, 100)])
classes = np.array(['Negative'] * 100 + ['Positive'] * 100)
example1 = pd.DataFrame({'prob': probs, 'class': classes})

sns.stripplot(data=example1, x='class', y='prob', jitter=True, alpha=0.6)
plt.ylabel("Predicted Probability of Positive")
plt.show()
```
:::

:::: {.column width="50%"}
```{python}
#| echo: false
y_true_binary = np.where(example1['class'] == 'Positive', 1, 0)
auc_val = roc_auc_score(y_true_binary, example1['prob'])

RocCurveDisplay.from_predictions(y_true_binary, example1['prob'])
plt.text(0.5, 0.2, f"AUC: {auc_val*100:.0f}%", fontsize=12)
plt.show()
```
:::
::::"""

part1_new = """```{python}
#| echo: false
#| fig-width: 10
#| fig-height: 4
np.random.seed(4025)
probs = np.concatenate([np.random.uniform(0, 0.1, 100), np.random.uniform(0.9, 1, 100)])
classes = np.array(['Negative'] * 100 + ['Positive'] * 100)
example1 = pd.DataFrame({'prob': probs, 'class': classes})
y_true_binary = np.where(example1['class'] == 'Positive', 1, 0)

auc_val = roc_auc_score(y_true_binary, example1['prob'])
fpr, tpr, _ = roc_curve(y_true_binary, example1['prob'])
roc_df = pd.DataFrame({'fpr': fpr, 'tpr': tpr})

p1 = (ggplot(example1, aes(x='class', y='prob'))
    + geom_jitter(alpha=0.6, width=0.2, height=0)
    + labs(y="Predicted Probability of Positive", x="")
)

p2 = (ggplot(roc_df, aes(x='fpr', y='tpr'))
    + geom_line(color="blue")
    + annotate('text', x=0.5, y=0.2, label=f"AUC: {auc_val*100:.0f}%", size=12)
    + labs(x="False Positive Rate", y="True Positive Rate")
)

(p1 | p2)
```"""

# Replace Ex 1 part 2
part2_old = """:::: columns
:::: {.column width="50%"}
```{python}
#| echo: false
threshold = 0

sns.stripplot(data=example1, x='class', y='prob', jitter=True, alpha=0.6)
plt.axhline(y=threshold, color='red')
plt.ylabel("Predicted Probability of Positive")
plt.show()
```
:::

:::: {.column width="50%"}
```{python}
#| echo: false
RocCurveDisplay.from_predictions(y_true_binary, example1['prob'])
plt.text(0.5, 0.2, f"AUC: {auc_val*100:.0f}%", fontsize=12)
plt.plot(1, 1, 'ro')
plt.show()
```
:::
::::"""

part2_new = """```{python}
#| echo: false
#| fig-width: 10
#| fig-height: 4
threshold = 0

p1_thresh = p1 + geom_hline(yintercept=threshold, color='red')
p2_thresh = p2 + annotate('point', x=1, y=1, color='red', size=3)

(p1_thresh | p2_thresh)
```"""

# Replace Ex 1 part 3
part3_old = """:::: columns
:::: {.column width="50%"}
```{python}
#| echo: false
threshold = 0.05

sns.stripplot(data=example1, x='class', y='prob', jitter=True, alpha=0.6)
plt.axhline(y=threshold, color='red')
plt.ylabel("Predicted Probability of Positive")
plt.show()
```
:::

:::: {.column width="50%"}
```{python}
#| echo: false
RocCurveDisplay.from_predictions(y_true_binary, example1['prob'])
plt.text(0.5, 0.2, f"AUC: {auc_val*100:.0f}%", fontsize=12)

fp_rate = np.sum((example1['class'] == 'Negative') & (example1['prob'] > threshold)) / 100
tp_rate = np.sum((example1['class'] == 'Positive') & (example1['prob'] > threshold)) / 100
plt.plot(fp_rate, tp_rate, 'ro')
plt.show()
```
:::
::::"""

part3_new = """```{python}
#| echo: false
#| fig-width: 10
#| fig-height: 4
threshold = 0.05

fp_rate = np.sum((example1['class'] == 'Negative') & (example1['prob'] > threshold)) / 100
tp_rate = np.sum((example1['class'] == 'Positive') & (example1['prob'] > threshold)) / 100

p1_thresh = p1 + geom_hline(yintercept=threshold, color='red')
p2_thresh = p2 + annotate('point', x=fp_rate, y=tp_rate, color='red', size=3)

(p1_thresh | p2_thresh)
```"""


# Replace Ex 1 part 4
part4_old = """:::: columns
:::: {.column width="50%"}
```{python}
#| echo: false
threshold = 0.5

sns.stripplot(data=example1, x='class', y='prob', jitter=True, alpha=0.6)
plt.axhline(y=threshold, color='red')
plt.ylabel("Predicted Probability of Positive")
plt.show()
```
:::

:::: {.column width="50%"}
```{python}
#| echo: false
RocCurveDisplay.from_predictions(y_true_binary, example1['prob'])
plt.text(0.5, 0.2, f"AUC: {auc_val*100:.0f}%", fontsize=12)

fp_rate = np.sum((example1['class'] == 'Negative') & (example1['prob'] > threshold)) / 100
tp_rate = np.sum((example1['class'] == 'Positive') & (example1['prob'] > threshold)) / 100
plt.plot(fp_rate, tp_rate, 'ro')
plt.show()
```
:::
::::"""

part4_new = """```{python}
#| echo: false
#| fig-width: 10
#| fig-height: 4
threshold = 0.5

fp_rate = np.sum((example1['class'] == 'Negative') & (example1['prob'] > threshold)) / 100
tp_rate = np.sum((example1['class'] == 'Positive') & (example1['prob'] > threshold)) / 100

p1_thresh = p1 + geom_hline(yintercept=threshold, color='red')
p2_thresh = p2 + annotate('point', x=fp_rate, y=tp_rate, color='red', size=3)

(p1_thresh | p2_thresh)
```"""

# Replace Ex 2
part5_old = """:::: columns
:::: {.column width="50%"}
```{python}
#| echo: false
np.random.seed(4025)
probs2 = np.concatenate([np.random.uniform(0, 0.5, 100), np.random.uniform(0.5, 1, 100)])
example2 = pd.DataFrame({'prob': probs2, 'class': classes})

sns.stripplot(data=example2, x='class', y='prob', jitter=True, alpha=0.6)
plt.ylabel("Predicted Probability of Positive")
plt.show()
```
:::

:::: {.column width="50%"}
```{python}
#| echo: false
auc_val2 = roc_auc_score(y_true_binary, example2['prob'])

RocCurveDisplay.from_predictions(y_true_binary, example2['prob'])
plt.text(0.5, 0.2, f"AUC: {auc_val2*100:.0f}%", fontsize=12)
plt.show()
```
:::
::::"""

part5_new = """```{python}
#| echo: false
#| fig-width: 10
#| fig-height: 4
np.random.seed(4025)
probs2 = np.concatenate([np.random.uniform(0, 0.5, 100), np.random.uniform(0.5, 1, 100)])
example2 = pd.DataFrame({'prob': probs2, 'class': classes})

auc_val2 = roc_auc_score(y_true_binary, example2['prob'])
fpr2, tpr2, _ = roc_curve(y_true_binary, example2['prob'])
roc_df2 = pd.DataFrame({'fpr': fpr2, 'tpr': tpr2})

p1_ex2 = (ggplot(example2, aes(x='class', y='prob'))
    + geom_jitter(alpha=0.6, width=0.2, height=0)
    + labs(y="Predicted Probability of Positive", x="")
)

p2_ex2 = (ggplot(roc_df2, aes(x='fpr', y='tpr'))
    + geom_line(color="blue")
    + annotate('text', x=0.5, y=0.2, label=f"AUC: {auc_val2*100:.0f}%", size=12)
    + labs(x="False Positive Rate", y="True Positive Rate")
)

(p1_ex2 | p2_ex2)
```"""

# EX 3
part6_old = """:::: columns
:::: {.column width="50%"}
```{python}
#| echo: false
np.random.seed(4025)
probs3 = np.concatenate([np.random.uniform(0, 0.7, 100), np.random.uniform(0.3, 1, 100)])
example3 = pd.DataFrame({'prob': probs3, 'class': classes})

sns.stripplot(data=example3, x='class', y='prob', jitter=True, alpha=0.6)
plt.ylabel("Predicted Probability of Positive")
plt.show()
```
:::

:::: {.column width="50%"}
```{python}
#| echo: false
auc_val3 = roc_auc_score(y_true_binary, example3['prob'])

RocCurveDisplay.from_predictions(y_true_binary, example3['prob'])
plt.text(0.5, 0.2, f"AUC: {auc_val3*100:.0f}%", fontsize=12)
plt.show()
```
:::
::::"""

part6_new = """```{python}
#| echo: false
#| fig-width: 10
#| fig-height: 4
np.random.seed(4025)
probs3 = np.concatenate([np.random.uniform(0, 0.7, 100), np.random.uniform(0.3, 1, 100)])
example3 = pd.DataFrame({'prob': probs3, 'class': classes})

auc_val3 = roc_auc_score(y_true_binary, example3['prob'])
fpr3, tpr3, _ = roc_curve(y_true_binary, example3['prob'])
roc_df3 = pd.DataFrame({'fpr': fpr3, 'tpr': tpr3})

p1_ex3 = (ggplot(example3, aes(x='class', y='prob'))
    + geom_jitter(alpha=0.6, width=0.2, height=0)
    + labs(y="Predicted Probability of Positive", x="")
)

p2_ex3 = (ggplot(roc_df3, aes(x='fpr', y='tpr'))
    + geom_line(color="blue")
    + annotate('text', x=0.5, y=0.2, label=f"AUC: {auc_val3*100:.0f}%", size=12)
    + labs(x="False Positive Rate", y="True Positive Rate")
)

(p1_ex3 | p2_ex3)
```"""

# EX 4
part7_old = """:::: columns
:::: {.column width="50%"}
```{python}
#| echo: false
np.random.seed(4025)
probs4 = np.concatenate([np.random.uniform(0, 1, 100), np.random.uniform(0, 1, 100)])
example4 = pd.DataFrame({'prob': probs4, 'class': classes})

sns.stripplot(data=example4, x='class', y='prob', jitter=True, alpha=0.6)
plt.ylabel("Predicted Probability of Positive")
plt.show()
```
:::

:::: {.column width="50%"}
```{python}
#| echo: false
auc_val4 = roc_auc_score(y_true_binary, example4['prob'])

RocCurveDisplay.from_predictions(y_true_binary, example4['prob'])
plt.text(0.5, 0.2, f"AUC: {auc_val4*100:.0f}%", fontsize=12)
plt.show()
```
:::
::::"""

part7_new = """```{python}
#| echo: false
#| fig-width: 10
#| fig-height: 4
np.random.seed(4025)
probs4 = np.concatenate([np.random.uniform(0, 1, 100), np.random.uniform(0, 1, 100)])
example4 = pd.DataFrame({'prob': probs4, 'class': classes})

auc_val4 = roc_auc_score(y_true_binary, example4['prob'])
fpr4, tpr4, _ = roc_curve(y_true_binary, example4['prob'])
roc_df4 = pd.DataFrame({'fpr': fpr4, 'tpr': tpr4})

p1_ex4 = (ggplot(example4, aes(x='class', y='prob'))
    + geom_jitter(alpha=0.6, width=0.2, height=0)
    + labs(y="Predicted Probability of Positive", x="")
)

p2_ex4 = (ggplot(roc_df4, aes(x='fpr', y='tpr'))
    + geom_line(color="blue")
    + annotate('text', x=0.5, y=0.2, label=f"AUC: {auc_val4*100:.0f}%", size=12)
    + labs(x="False Positive Rate", y="True Positive Rate")
)

(p1_ex4 | p2_ex4)
```"""

# EX 5
part8_old = """:::: columns
:::: {.column width="50%"}
```{python}
#| echo: false
np.random.seed(4025)
a, b = 1, 3
probs5 = np.concatenate([np.random.beta(a, b, 100), np.random.beta(b, a, 100)])
example5 = pd.DataFrame({'prob': probs5, 'class': classes})

sns.stripplot(data=example5, x='class', y='prob', jitter=True, alpha=0.6)
plt.ylabel("Predicted Probability of Positive")
plt.show()
```
:::

:::: {.column width="50%"}
```{python}
#| echo: false
auc_val5 = roc_auc_score(y_true_binary, example5['prob'])

RocCurveDisplay.from_predictions(y_true_binary, example5['prob'])
plt.text(0.5, 0.2, f"AUC: {auc_val5*100:.0f}%", fontsize=12)
plt.show()
```
:::
::::"""

part8_new = """```{python}
#| echo: false
#| fig-width: 10
#| fig-height: 4
np.random.seed(4025)
a, b = 1, 3
probs5 = np.concatenate([np.random.beta(a, b, 100), np.random.beta(b, a, 100)])
example5 = pd.DataFrame({'prob': probs5, 'class': classes})

auc_val5 = roc_auc_score(y_true_binary, example5['prob'])
fpr5, tpr5, _ = roc_curve(y_true_binary, example5['prob'])
roc_df5 = pd.DataFrame({'fpr': fpr5, 'tpr': tpr5})

p1_ex5 = (ggplot(example5, aes(x='class', y='prob'))
    + geom_jitter(alpha=0.6, width=0.2, height=0)
    + labs(y="Predicted Probability of Positive", x="")
)

p2_ex5 = (ggplot(roc_df5, aes(x='fpr', y='tpr'))
    + geom_line(color="blue")
    + annotate('text', x=0.5, y=0.2, label=f"AUC: {auc_val5*100:.0f}%", size=12)
    + labs(x="False Positive Rate", y="True Positive Rate")
)

(p1_ex5 | p2_ex5)
```"""

# EX 6
part9_old = """:::: columns
:::: {.column width="50%"}
```{python}
#| echo: false
np.random.seed(4025)
a, b = 2, 3
probs6 = np.concatenate([np.random.beta(a, b, 100), np.random.beta(b, a, 100)])
example6 = pd.DataFrame({'prob': probs6, 'class': classes})

sns.stripplot(data=example6, x='class', y='prob', jitter=True, alpha=0.6)
plt.ylabel("Predicted Probability of Positive")
plt.show()
```
:::

:::: {.column width="50%"}
```{python}
#| echo: false
auc_val6 = roc_auc_score(y_true_binary, example6['prob'])

RocCurveDisplay.from_predictions(y_true_binary, example6['prob'])
plt.text(0.5, 0.2, f"AUC: {auc_val6*100:.0f}%", fontsize=12)
plt.show()
```
:::
::::"""

part9_new = """```{python}
#| echo: false
#| fig-width: 10
#| fig-height: 4
np.random.seed(4025)
a, b = 2, 3
probs6 = np.concatenate([np.random.beta(a, b, 100), np.random.beta(b, a, 100)])
example6 = pd.DataFrame({'prob': probs6, 'class': classes})

auc_val6 = roc_auc_score(y_true_binary, example6['prob'])
fpr6, tpr6, _ = roc_curve(y_true_binary, example6['prob'])
roc_df6 = pd.DataFrame({'fpr': fpr6, 'tpr': tpr6})

p1_ex6 = (ggplot(example6, aes(x='class', y='prob'))
    + geom_jitter(alpha=0.6, width=0.2, height=0)
    + labs(y="Predicted Probability of Positive", x="")
)

p2_ex6 = (ggplot(roc_df6, aes(x='fpr', y='tpr'))
    + geom_line(color="blue")
    + annotate('text', x=0.5, y=0.2, label=f"AUC: {auc_val6*100:.0f}%", size=12)
    + labs(x="False Positive Rate", y="True Positive Rate")
)

(p1_ex6 | p2_ex6)
```"""


content = content.replace(part1_old, part1_new)
content = content.replace(part2_old, part2_new)
content = content.replace(part3_old, part3_new)
content = content.replace(part4_old, part4_new)
content = content.replace(part5_old, part5_new)
content = content.replace(part6_old, part6_new)
content = content.replace(part7_old, part7_new)
content = content.replace(part8_old, part8_new)
content = content.replace(part9_old, part9_new)

with open('slides/10-roc-auc.qmd', 'w') as f:
    f.write(content)

print('Success')
