import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import sys
sns.set_style({'axes.grid':False})
sns.set(style='ticks', rc={'lines.linewidth':3})

def main():
    csv_file = sys.argv[1]
    label = sys.argv[2]
    df = pd.read_csv(csv_file)

    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, \
            gridspec_kw={"height_ratios": (.15, .85)})
    f.set_figheight(9)
    f.set_figwidth(10)
    sns.boxplot(df[label],ax=ax_box)
    sns.distplot(df[label],ax=ax_hist)
    ax_box.set(xlabel='')

    plt.title('',fontsize=25)
    plt.ylabel('')
    plt.xlabel(label, fontsize=17)
    plt.tight_layout()
    plt.savefig('plot.png',format="png")


if __name__ == "__main__":
    main()
