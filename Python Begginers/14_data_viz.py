#import libraries
import seaborn as sns
import matplotlib.pyplot as plt

#setup-2 set a theme
sns.set_theme(style="ticks",color_codes=True)

#setup-3 
kashti=sns.load_dataset("titanic")
print(kashti)

#setup-4
p=sns.countplot(x="sex",data=kashti)
plt.show()

#step-5 plot basic graph with 2 variables 
p=sns.countplot(x="sex",data=kashti,hue="class")
p.set_title("count plot for kashti")
plt.show()



#step-6 plot basic graph with 2 variable (count plot) with titles
p=sns.countplot(x="sex",data=kashti,hue="class")
p.set_title("count plot for kashti")
plt.show()