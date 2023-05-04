using MahApps.Metro.Controls;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Diagnostics;

namespace SmartHomeMonitoringApp
{
    /// <summary>
    /// MainWindow.xaml에 대한 상호 작용 논리
    /// </summary>
    public partial class MainWindow : MetroWindow
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void MetroWindow_Loaded(object sender, RoutedEventArgs e)
        {
            // <Frame> ==> Page.xaml
            // 
            ActiveItem.Content = new Views.DataBaseMonPage();
        }

        // 끝내기 버튼 클릭이벤트 핸들러
        private void MnuExitSubScribe_Click(object sender, RoutedEventArgs e)
        {
            Process.GetCurrentProcess().Kill(); // 작업관리자에서 프로세스 종료
            Environment.Exit(0); // 둘 중 하나만 쓰면 됨

        }
    }
}
