from matplotlib import pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
import matplotlib

# 단순 차트
plt.plot([1, 2, 3], [110, 130, 120]) # plt.plot(x, y)
# plt.show()
plt.clf()  # plt 초기화 (초기화를 해 주지 않은 경우 위의 plot이 아래에 영향을 주게 된다.

# title and lable
plt.plot(["Seoul", "Paris", "Seattle"], [30, 25, 55])
plt.xlabel('City')
plt.ylabel('Response')
plt.title('Experiment Result')
# plt.show()
plt.clf()

# legend
plt.plot([1, 2, 3], [1, 4, 9])  # Mouse
plt.plot([2, 3, 4], [5, 6, 7])  # Cat
plt.xlabel('Sequence')
plt.ylabel('Time(secs)')
plt.title('Experiment Result')
plt.legend(['Mouse', 'Cat'])
# plt.show()
plt.clf()

# rc 활용 (https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.rc.html)
# 폰트설정
# path = "c:/Windows/Fonts/malgun.ttf"
# font_name = font_manager.FontProperties(fname=path).get_name()
# rc('font', family=font_name)
# # or  matplotlib.rc('font',family=font_name)

# plt.rc('legend', fontsize=16)


# bar Chart
y = [5, 3, 7, 10, 9, 5, 3.5, 8]
x = range(len(y))
plt.grid(True)
plt.bar(x, y, width=0.7, color="blue")
plt.show()
plt.clf()


# subplot

plt.subplot(2, 1, 1)                # nrows=2, ncols=1, index=1
plt.title('2, 1, 1')
plt.subplot(2, 1, 2)                # nrows=2, ncols=1, index=2
plt.title('22, 1, 2')

plt.subplot(1, 2, 1)                # nrows=2, ncols=1, index=2
plt.title('1, 2, 1')
plt.subplot(1, 2, 2)                # nrows=2, ncols=1, index=2
plt.title('1, 2, 2')

plt.subplot(2, 2, 1)
plt.title('2, 2, 1')
plt.subplot(2, 2, 2)
plt.title('2, 2, 2')
plt.subplot(2, 2, 3)
plt.title('2, 2, 3')
plt.subplot(2, 2, 4)
plt.title('2, 2, 4')

plt.tight_layout()
# plt.show()
plt.clf()

# subplot
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

plt.subplot(2, 1, 1)                # nrows=2, ncols=1, index=1
# plt.plot(x1, y1, 'o-')
plt.title('1st Graph')
# plt.ylabel('Damped oscillation')

plt.subplot(2, 1, 2)                # nrows=2, ncols=1, index=2
# plt.plot(x2, y2, '.-')
# plt.title('2nd Graph')
# plt.xlabel('time (s)')
# plt.ylabel('Undamped')

plt.tight_layout()
# plt.show()
plt.clf()


x = np.arange(0, 2, 0.2)

plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(x, x**3, color='forestgreen', marker='^', markersize=9)
plt.xticks([0, 1, 2])
plt.yticks(np.arange(1, 6))
# plt.show()
plt.clf()


x = np.arange(0, 2, 0.2)
plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(x, x**3, color='springgreen', marker='^', markersize=9)
plt.xticks(np.arange(0, 2, 0.2), labels=['Jan', '', 'Feb', '', 'Mar', '', 'May', '', 'June', ''])
plt.yticks(np.arange(0, 7), ('0', '1GB', '2GB', '3GB', '4GB', '5GB', '6GB'))
# plt.show()
plt.clf()

x = np.arange(0, 2, 0.2)

plt.plot(x, x, 'bo')
plt.plot(x, x**2, color='#e35f62', marker='*', linewidth=2)
plt.plot(x, x**3, color='springgreen', marker='^', markersize=9)
plt.xticks(np.arange(0, 2, 0.2), labels=['Jan', '', 'Feb', '', 'Mar', '', 'May', '', 'June', ''])
plt.yticks(np.arange(0, 7), ('0', '1GB', '2GB', '3GB', '4GB', '5GB', '6GB'))
# plt.show()


