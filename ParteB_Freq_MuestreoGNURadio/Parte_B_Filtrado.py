#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: LAB1_ParteB_Punto6
# Author: DiegoEspinel_DiegoGarcia_B1A_G2
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import audio
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip



class Parte_B_Filtrado(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "LAB1_ParteB_Punto6", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("LAB1_ParteB_Punto6")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "Parte_B_Filtrado")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 200000
        self.audio_rate = audio_rate = 44093
        self.Fc = Fc = 1500
        self.F_corte = F_corte = 1500
        self.BW = BW = 1500

        ##################################################
        # Blocks
        ##################################################

        self._samp_rate_range = qtgui.Range(1000, 300000, 1000, 200000, 200)
        self._samp_rate_win = qtgui.RangeWidget(self._samp_rate_range, self.set_samp_rate, "Frecuencia de Muestreo", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._samp_rate_win)
        self._Fc_range = qtgui.Range(100, 21000, 10, 1500, 200)
        self._Fc_win = qtgui.RangeWidget(self._Fc_range, self.set_Fc, "Frecuencia Central", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Fc_win)
        self._BW_range = qtgui.Range(10, 50000, 10, 1500, 200)
        self._BW_win = qtgui.RangeWidget(self._BW_range, self.set_BW, "Ancho de Banda", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._BW_win)
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=audio_rate,
                decimation=samp_rate,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=samp_rate,
                decimation=audio_rate,
                taps=[],
                fractional_bw=0)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            2,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['Interpolación', 'Diezmado', '', '', '',
            '', '', '', '', '']
        widths = [2, 2, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('D:\\INGENIERIA ELECTRONICA\\11. Onceavo Semestre\\Comunicaciones I\\LABS Comu I\\Laboratorio_1\\ParteB_Freq_MuestreoGNURadio\\gitana_williecolon.wav', True)
        self.band_pass_filter_0 = filter.interp_fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                (Fc-BW/2),
                (Fc+BW/2),
                100,
                window.WIN_HAMMING,
                6.76))
        self.audio_sink_0 = audio.sink(audio_rate, '', True)
        self._F_corte_range = qtgui.Range(100, 21000, 10, 1500, 200)
        self._F_corte_win = qtgui.RangeWidget(self._F_corte_range, self.set_F_corte, "Frecuencia de Corte", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._F_corte_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.band_pass_filter_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.audio_sink_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Parte_B_Filtrado")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.Fc-self.BW/2), (self.Fc+self.BW/2), 100, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate

    def get_Fc(self):
        return self.Fc

    def set_Fc(self, Fc):
        self.Fc = Fc
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.Fc-self.BW/2), (self.Fc+self.BW/2), 100, window.WIN_HAMMING, 6.76))

    def get_F_corte(self):
        return self.F_corte

    def set_F_corte(self, F_corte):
        self.F_corte = F_corte

    def get_BW(self):
        return self.BW

    def set_BW(self, BW):
        self.BW = BW
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, (self.Fc-self.BW/2), (self.Fc+self.BW/2), 100, window.WIN_HAMMING, 6.76))




def main(top_block_cls=Parte_B_Filtrado, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
