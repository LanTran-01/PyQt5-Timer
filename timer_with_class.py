import sys
from PyQt5.QtCore import Qt,QTimer, QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout,QHBoxLayout, QMessageBox, QLabel, QGridLayout, QStackedWidget, QMainWindow
from PyQt5.QtMultimedia import QSoundEffect

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desktop Timer")

        self.time_unfiltered = 0
        self.def_hour = 0
        self.def_minute = 0
        self.def_second = 0
        self.hour = 0
        self.minute = 0
        self.second = 0

        self.stacked_widget = QStackedWidget()

        self.widget1 = QWidget()
        
        self.screen_layout = QVBoxLayout(self.widget1)
        self.screen = QLabel(f'{self.hour:02}:{self.minute:02}:{self.second:02}')
        self.screen.setStyleSheet("background-color: black; color: white; font-size: 48px;")
        self.screen.setAlignment(Qt.AlignCenter)
        self.screen.setFixedHeight(70)
        self.screen_layout.addWidget(self.screen)

        self.button_layout = QHBoxLayout()
        self.start_timer = QPushButton('Start')
        self.stop_timer = QPushButton('Stop')
        self.clear_timer = QPushButton('Clear')
        self.set_timer = QPushButton('Set')
        self.button_layout.addWidget(self.start_timer)
        self.button_layout.addWidget(self.stop_timer)
        self.button_layout.addWidget(self.clear_timer)
        self.button_layout.addWidget(self.set_timer)
        self.screen_layout.addLayout(self.button_layout)
        self.stacked_widget.addWidget(self.widget1)

        self.widget2 = QWidget()

        self.setting_layout = QVBoxLayout(self.widget2)
        self.set_screen = QLabel('00:00:00')
        self.set_screen.setStyleSheet("background-color: black; color: white; font-size: 48px;")
        self.set_screen.setAlignment(Qt.AlignCenter)
        self.set_screen.setFixedHeight(70)
        self.setting_layout.addWidget(self.set_screen)

        self.setting_buttons_layout = QGridLayout()

        self.button_1 = QPushButton('1')
        self.button_2 = QPushButton('2')
        self.button_3 = QPushButton('3')
        self.button_4 = QPushButton('4')
        self.button_5 = QPushButton('5')
        self.button_6 = QPushButton('6')
        self.button_7 = QPushButton('7')
        self.button_8 = QPushButton('8')
        self.button_9 = QPushButton('9')
        self.button_0 = QPushButton('0')
        self.button_clear = QPushButton('X')
        self.button_set = QPushButton('|>')

        self.setting_buttons_layout.addWidget(self.button_1, 0, 0)
        self.setting_buttons_layout.addWidget(self.button_2, 0, 1)
        self.setting_buttons_layout.addWidget(self.button_3, 0, 2)
        self.setting_buttons_layout.addWidget(self.button_4, 1, 0)
        self.setting_buttons_layout.addWidget(self.button_5, 1, 1)
        self.setting_buttons_layout.addWidget(self.button_6, 1, 2)
        self.setting_buttons_layout.addWidget(self.button_7, 2, 0)
        self.setting_buttons_layout.addWidget(self.button_8, 2, 1)
        self.setting_buttons_layout.addWidget(self.button_9, 2, 2)
        self.setting_buttons_layout.addWidget(self.button_clear, 3,0 )
        self.setting_buttons_layout.addWidget(self.button_0, 3, 1)
        self.setting_buttons_layout.addWidget(self.button_set, 3, 2)

        self.setting_layout.addLayout(self.setting_buttons_layout)
        self.stacked_widget.addWidget(self.widget2)
        self.stacked_widget.setCurrentWidget(self.widget2)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.stacked_widget)
        self.setLayout(main_layout)

        self.time_up_sound = QSoundEffect()
        self.time_up_sound.setSource(QUrl.fromLocalFile('TF002.wav'))
        self.time_up_sound.setVolume(0.5)

        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_interrupt)
        self.start_timer.clicked.connect(self.start_timer_timer)
        self.stop_timer.clicked.connect(self.stop_timer_timer)
        self.clear_timer.clicked.connect(self.reset_timer)
        self.button_set.clicked.connect(self.button_set_clicked)
        self.set_timer.clicked.connect(self.set_timer_clicked)
        self.button_0.clicked.connect(lambda: self.set_timer_func(0))
        self.button_1.clicked.connect(lambda: self.set_timer_func(1))
        self.button_2.clicked.connect(lambda: self.set_timer_func(2))
        self.button_3.clicked.connect(lambda: self.set_timer_func(3))
        self.button_4.clicked.connect(lambda: self.set_timer_func(4))
        self.button_5.clicked.connect(lambda: self.set_timer_func(5))
        self.button_6.clicked.connect(lambda: self.set_timer_func(6))
        self.button_7.clicked.connect(lambda: self.set_timer_func(7))
        self.button_8.clicked.connect(lambda: self.set_timer_func(8))
        self.button_9.clicked.connect(lambda: self.set_timer_func(9))
        self.button_clear.clicked.connect(lambda: self.set_timer_func(-1))



    def timer_interrupt(self):
        done = 0
        if (self.second == 0):
            if(self.minute == 0):
                if(self.hour == 0):
                    self.timer.stop()
                    done = 1
                else:
                    self.hour = self.hour - 1
                    self.minute = 59
                    self.second = 59
            else:
                self.minute = self.minute - 1
                self.second = 59
        else:
            self.second = self.second - 1
        if (done == 0) :
            self.screen.setText(f'{self.hour:02}:{self.minute:02}:{self.second:02}')
        else: 
            self.screen.setText("Time's up")
            self.time_up_sound.play()
    


    def start_timer_timer(self):
        self.timer.start(1000)


    
    def stop_timer_timer(self):
        self.timer.stop()



    def reset_timer(self):
        self.timer.stop()
        self.hour = self.def_hour
        self.minute = self.def_minute
        self.second = self.def_second
        self.screen.setText(f'{self.hour:02}:{self.minute:02}:{self.second:02}')
        self.time_up_sound.stop()

    

    def button_set_clicked(self):
        self.stacked_widget.setCurrentWidget(self.widget1)

        if(self.def_second >= 60):
            self.def_second = self.def_second - 60
            self.def_minute = self.def_minute + 1 

        if(self.def_minute >= 60):
            self.def_minute = self.def_minute - 60
            self.def_hour = self.def_hour + 1
    
        self.hour = self.def_hour
        self.minute = self.def_minute
        self.second = self.def_second

        self.screen.setText(f'{self.hour:02}:{self.minute:02}:{self.second:02}')



    def set_timer_clicked(self):
        self.stacked_widget.setCurrentWidget(self.widget2)
        self.time_unfiltered = 0
        self.time_unfiltered = self.def_second + 100 * self.def_minute + 10000 * self.def_hour
        self.set_screen.setText(f'{self.hour:02}:{self.minute:02}:{self.second:02}')



    def set_timer_func(self,digit):
        if(digit == -1):
            self.time_unfiltered = 0
        else:
            self.time_unfiltered = self.time_unfiltered * 10 + digit
            self.time_unfiltered = self.time_unfiltered % 1000000

        self.def_second = self.time_unfiltered % 100
        self.def_minute = (int(self.time_unfiltered/100))%100
        self.def_hour = int((self.time_unfiltered/10000))%100

        self.set_screen.setText(f'{self.def_hour:02}:{self.def_minute:02}:{self.def_second:02}')
    


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()