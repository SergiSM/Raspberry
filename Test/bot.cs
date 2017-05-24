using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        PictureBox pic = new PictureBox();
        string CURRENT_PANEL = "p_0_0";
        
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int x = 20;
            int y = 80;
            for (int i = 0; i < 10; i++)
            {
                for (int j = 0; j < 10; j++)
                {
                    Panel p = new Panel();
                    p.Width = 50;
                    p.Height = 50;
                    p.Name = "p_"+i+"_"+j;

                    if ((j % 2) == 0)
                        p.BackColor = Color.LightBlue;
                    else
                        p.BackColor = Color.White;
                    p.BorderStyle = BorderStyle.FixedSingle;
                    p.Location = new Point(x,y);
                    p.Click += new EventHandler(panel_Click);
                    x += 50;                    
                    
                    if ((i == 0) && (j == 0))
                    {                        
                        pic.Image = Image.FromFile(@"C:\Users\externo101\Documents\PROVES_SERGI\BOT\WindowsFormsApplication1\WindowsFormsApplication1\bin\Debug\bee.bmp");
                        pic.Size = new Size(30, 30);
                        pic.Location = new Point(10, 10);
                        p.Controls.Add(pic);
                    }

                    this.Controls.Add(p);
                }
                x = 20;
                y += 50; 
            }            
        }

        void panel_Click(object sender, EventArgs e)
        {
            //Panel p = this.Controls.Find(CURRENT_PANEL, true)[0] as Panel;
        }

        private void b_up_Click(object sender, EventArgs e)
        {
            listBox1.Items.Add("up");
        }

        private void b_left_Click(object sender, EventArgs e)
        {
            listBox1.Items.Add("left");
        }

        private void b_right_Click(object sender, EventArgs e)
        {
            listBox1.Items.Add("right");            
        }

        private void b_down_Click(object sender, EventArgs e)
        {
            listBox1.Items.Add("down");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            timer1.Enabled = true;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (listBox1.Items.Count == 0)
                timer1.Enabled = false;
            else             
            {                
                Moviment(listBox1.Items[0].ToString());               

                listBox1.Items.RemoveAt(0); //fifo
            }
        }

        private void Moviment(string mov)
        {
            Panel p = this.Controls.Find(CURRENT_PANEL, true)[0] as Panel;
            p.Controls.RemoveAt(0);

            string[] s = CURRENT_PANEL.Split('_');

            switch (mov)
            {
                case "up" :                        
                        CURRENT_PANEL = "p_" + (Convert.ToInt32(s[1]) - 1) + "_" + s[2];
                    break;

                case "down":
                    CURRENT_PANEL = "p_" + (Convert.ToInt32(s[1]) + 1) + "_" + s[2];
                    break;

                case "left":
                    CURRENT_PANEL = "p_" + s[1] + "_" + (Convert.ToInt32(s[2]) - 1);
                    break;

                case "right":
                    CURRENT_PANEL = "p_" + s[1] + "_" + (Convert.ToInt32(s[2]) + 1);
                    break;
            }

            Panel p2 = this.Controls.Find(CURRENT_PANEL, true)[0] as Panel;
            p2.Controls.Add(pic);
        }

    }
}
