namespace ConsoleApplication1
{
    class Program
    {
        //https://stackoverflow.com/questions/836427/how-to-run-a-c-sharp-console-application-with-the-console-hidden
        //Go to your console app's properties(project's properties).In the "Application" tab, just change the "Output type" to "Windows Application".
        
        static List<string> llista = new List<string>();        
        
        static void Main(string[] args)
        {
            //Timer timer = new Timer(TimerCallback, null, 0, 3000);
            Finestres();

            

            File.AppendAllText("C:\\Temp\\log.txt", "************************************\n");
            File.AppendAllText("C:\\Temp\\log.txt", DateTime.Now.ToShortTimeString()+"\n");
            File.AppendAllLines("C:\\Temp\\log.txt", llista);            
        }

        private static void TimerCallback(Object o)
        {
            // Display the date/time when this method got called.
            Console.WriteLine("In TimerCallback: " + DateTime.Now);
            // Force a garbage collection to occur for this demo.
            GC.Collect();
        }

        static private void Finestres()
        {                       
            Process[] processes = Process.GetProcesses();
            foreach (Process p in processes)
            {
                if (!String.IsNullOrEmpty(p.MainWindowTitle))
                {
                    llista.Add(p.MainWindowTitle);
                }
            }

            //https://social.msdn.microsoft.com/Forums/en-US/eaef0ea6-9426-45ca-a5f0-b9bc5c53b84e/how-to-get-all-open-tabs-in-google-chrome?forum=csharpgeneral
            Process[] procsChrome = Process.GetProcessesByName("chrome");
            if (procsChrome.Length <= 0)
            {
                Console.WriteLine("Chrome is not running");
            }
            else
            {
                foreach (Process proc in procsChrome)
                {
                    // the chrome process must have a window 
                    if (proc.MainWindowHandle == IntPtr.Zero)
                    {
                        continue;
                    }

                    try
                    {
                        /*AutomationElement root = AutomationElement.FromHandle(proc.MainWindowHandle);
                        Condition condition = new PropertyCondition(AutomationElement.ControlTypeProperty, ControlType.Window);
                        var tabs = root.FindAll(TreeScope.Descendants, condition);*/

                        // to find the tabs we first need to locate something reliable - the 'New Tab' button 
                        AutomationElement root = AutomationElement.FromHandle(proc.MainWindowHandle);
                        //Condition condNewTab = new PropertyCondition(AutomationElement.NameProperty, "New Tab");
                        Condition condNewTab = new PropertyCondition(AutomationElement.NameProperty, "Nueva pestaña");
                        AutomationElement elmNewTab = root.FindFirst(TreeScope.Descendants, condNewTab);
                        // get the tabstrip by getting the parent of the 'new tab' button 
                        TreeWalker treewalker = TreeWalker.ControlViewWalker;
                        AutomationElement elmTabStrip = treewalker.GetParent(elmNewTab);
                        // loop through all the tabs and get the names which is the page title 
                        Condition condTabItem = new PropertyCondition(AutomationElement.ControlTypeProperty, ControlType.TabItem);
                        foreach (AutomationElement tabitem in elmTabStrip.FindAll(TreeScope.Children, condTabItem))
                        {
                            Console.WriteLine(tabitem.Current.Name);
                            llista.Add(tabitem.Current.Name);
                        }
                    }
                    catch { }
                }
            }

 }


    }
}
