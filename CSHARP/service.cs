using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.ServiceProcess;
using System.Text;
using System.Threading.Tasks;

namespace WindowsService1
{
    public partial class Service1 : ServiceBase
    {
        private int n_items = -1;
        List<string> llista = new List<string>();
        
        public Service1()
        {
            InitializeComponent();


        }

        protected override void OnStart(string[] args)
        {
            StreamWriter tw = new StreamWriter("c:\\Temp\\log2.txt");
            tw.Write("**");
            tw.Close();
            timer1.Enabled = true;
        }

        protected override void OnStop()
        {
        }

        private void Finestres()
        {
            llista.Clear();
            Process[] processes = Process.GetProcesses();
            foreach (Process p in processes)
            {
                if (!String.IsNullOrEmpty(p.MainWindowTitle))
                {
                    llista.Add(p.MainWindowTitle);
                }
            }

            /*WebClient client = new WebClient();
            if (listBox1.Items.Count > 9)   //he de mirar quans items hi ha en repòs
            {                
            }*/
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Finestres();

            //if (n_items > -1)
            //{
                /*if (llista.Count != n_items)
                {
                    label1.Text = "canvi";                  
                }
                else
                    label1.Text = "-";*/

                StreamWriter tw = new StreamWriter("c:\\Temp\\log.txt");
                for (int i = 0; i < llista.Count; i++)
                    tw.Write(DateTime.Now.ToShortTimeString()+" = "+llista[i]+"\n");
                tw.Close();
            //}
            n_items = llista.Count;
        }
    }
}
