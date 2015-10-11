    using System;
    using System.Collections;
    using System.Collections.Generic;
     
    namespace Network
    {
        public class IP {
            private byte A;
            private byte B;
            private byte C;
            private byte D;
        }
     
        public class Desktop
        {
            public int[] ip;
            public string hostname;
     
            public Desktop(string hostname)
            {
                ip = new int[4];
                this.hostname = hostname;
            }
        }
     
        public class LAN : IEnumerable<Desktop>
        {
            public int[] ip = new int[4];
            public string hostname;
            Dictionary<string, Desktop> workstations;
            Dictionary<string, int[]> staticIP;
     
            public LAN(string hostname)
            {
                this.hostname = hostname;
                workstations = new Dictionary<string, Desktop>();
                staticIP = new Dictionary<string, int[]>();
            }
     
            public int Count { get { return workstations.Count; } }
     
            public IEnumerator<Desktop> GetEnumerator()
            {
                foreach (var i in workstations)
                {
                    yield return i.Value;
                }
            }
     
            IEnumerator IEnumerable.GetEnumerator()
            {
                return GetEnumerator();
            }
     
            public void Add(string hostname, Desktop item)
            {
                if (staticIP.ContainsKey(item.hostname))
                {
                    staticIP.TryGetValue(item.hostname, out item.ip);
                }
                else
                {
                    item.ip[0] = 192;
                    item.ip[1] = 168;
                    item.ip[2] = this.ip[3];
                    item.ip[3] = Count + 1;
                    while(true)
                    {
                        foreach (KeyValuePair<string, int[]> i in staticIP)
                        {
                            if (item.ip[3] == i.Value[3])
                            {
                                item.ip[3] = item.ip[3] + 1;
                            }
                        }
                        break;
                    }
                }
                workstations.Add(hostname, item);
            }
     
            public bool Remove(string hostname)
            {
                return workstations.Remove(hostname);
            }
     
            public void Clear()
            {
                workstations.Clear();
                staticIP.Clear();
            }
     
            public bool ContainsKey(string hostname)
            {
                return workstations.ContainsKey(hostname);
            }
     
            public bool TryGetValue(string hostname, out Desktop item)
            {
                return workstations.TryGetValue(hostname, out item);
            }
     
            public void MoveTo(string hostname, LAN network)
            {
                Desktop item;
                if (workstations.TryGetValue(hostname, out item))
                {
                    network.Add(hostname, item);
                    Remove(hostname);
                }
            }
     
            public void SetStaticIP(string hostname)
            {
                Desktop foundDesktop;
                if (workstations.TryGetValue(hostname, out foundDesktop))
                {
                    staticIP.Add(foundDesktop.hostname, foundDesktop.ip);
                }
            }
     
            public void UnsetStaticIP(string hostname)
            {
                if (workstations.ContainsKey(hostname) && staticIP.ContainsKey(hostname))
                {
                    staticIP.Remove(hostname);
                }
            }
     
            public void Show()
            {
                foreach (KeyValuePair<string, Desktop> i in workstations )
                {
                    Console.WriteLine("     {0} - {1}.{2}.{3}.{4}", i.Value.hostname, i.Value.ip[0], i.Value.ip[1], i.Value.ip[2], i.Value.ip[3]);
                }
            }
        }
     
        public class MAN : IEnumerable<LAN>
        {
            private Dictionary<string, LAN> localNetworks;
     
            public MAN()
            {
                localNetworks = new Dictionary<string, LAN>();
            }
     
            public IEnumerator<LAN> GetEnumerator()
            {
                foreach (KeyValuePair<string, LAN> i in localNetworks)
                {
                    yield return i.Value;
                }
            }
     
            IEnumerator IEnumerable.GetEnumerator()
            {
                return GetEnumerator();
            }
     
            public int Count { get { return localNetworks.Count; } }
     
            public void Add(string hostname, LAN item)
            {
                item.ip[0] = 192;
                item.ip[1] = 168;
                item.ip[2] = 0;
                item.ip[3] = localNetworks.Count + 1;
                localNetworks.Add(hostname, item);
            }
     
            public bool Remove(string hostname)
            {
                if (localNetworks.ContainsKey(hostname))
                {
                    localNetworks.Remove(hostname);
                    return true;
                }
                else
                {
                    return false;
                }
            }
     
            public void Clear()
            {
                localNetworks.Clear();
            }  
     
            public bool ContainsKey(string hostname)
            {
                return localNetworks.ContainsKey(hostname);
            }
     
            public bool TryGetValue(string hostname, out LAN local)
            {
                return localNetworks.TryGetValue(hostname, out local);
            }
     
            public void Show()
            {
                foreach (KeyValuePair<string, LAN> i in localNetworks)
                {
                    Console.WriteLine("{0} - {1}.{2}.{3}.{4}", i.Value.hostname, i.Value.ip[0], i.Value.ip[1], i.Value.ip[2], i.Value.ip[3]);
                    i.Value.Show();
                }
            }
     
            public void Combine(string selectedLAN1, string selectedLAN2)
            {
                LAN foundLAN1;
                LAN foundLAN2;
     
                if (localNetworks.TryGetValue(selectedLAN1, out foundLAN1) && localNetworks.TryGetValue(selectedLAN2, out foundLAN2))
                {
                    foreach (Desktop i in foundLAN2)
                    {
                       foundLAN1.Add(i.hostname, i);                  
                    }
                    foundLAN2.Clear();
                    localNetworks.Remove(selectedLAN2);
                }
            }
        }
     
        public class Test
        {
            public static void Main()
            {
                MAN Minsk = new MAN();
                ConsoleKeyInfo actkey;
                bool exit = false;
     
                while (!exit)
                {
                    LAN foundLAN;
                    LAN foundLAN2;
                    string selectedLAN1;
                    string selectedLAN2;
                    string selectedHostname;
     
                    Console.Clear();
                    Console.WriteLine("Press Q to add new LAN");
                    Console.WriteLine("Press W to add new Desktop");
                    Console.WriteLine("Press E to remove Desktop");
                    Console.WriteLine("Press R to move Desktop to another LAN");
                    Console.WriteLine("Press T to Clear everything");
                    Console.WriteLine("Press Y to Clear LAN");
                    Console.WriteLine("Press U to set static ip in some LAN for Desktop");
                    Console.WriteLine("Press I to unset static ip in some LAN for Desktop");
                    Console.WriteLine("Press O to combine two LAN's");
                    Console.WriteLine("Press Esc to exit");
                    Console.WriteLine("\n\n");
                    Minsk.Show();
     
                    actkey = Console.ReadKey();
     
                    switch (actkey.Key)
                    {
                        case ConsoleKey.Q:
                            Console.WriteLine("Please, enter the hostname of new LAN");
                            selectedLAN1 = Console.ReadLine();
                            Minsk.Add(selectedLAN1, new LAN(selectedLAN1));
                            break;
                        case ConsoleKey.W:
                            if (Minsk.Count != 0)
                            {
                                Console.WriteLine("Please, enter hostname of new Desktop and hostname of LAN");
                                selectedHostname = Console.ReadLine();
                                selectedLAN1 = Console.ReadLine();
     
                                if (Minsk.TryGetValue(selectedLAN1, out foundLAN))
                                {
                                    foundLAN.Add(selectedHostname, new Desktop(selectedHostname));
                                }
                            }
                            break;
                        case ConsoleKey.E:
                            Console.WriteLine("Please, enter hostname of removed Desktop and hostname of LAN");
                            selectedHostname = Console.ReadLine();
                            selectedLAN1 = Console.ReadLine();
     
                            if (Minsk.TryGetValue(selectedLAN1, out foundLAN))
                            {
                                foundLAN.Remove(selectedHostname);
                            }
                            break;
                        case ConsoleKey.R:
                            Console.WriteLine("Please, enter hostname of moved Desktop, hostname of LAN of this Desktop and hostname of new LAN");
                            selectedHostname = Console.ReadLine();
                            selectedLAN1 = Console.ReadLine();
                            selectedLAN2 = Console.ReadLine();
     
                            if (Minsk.TryGetValue(selectedLAN1, out foundLAN) && Minsk.TryGetValue(selectedLAN2, out foundLAN2))
                            {
                                foundLAN.MoveTo(selectedHostname, foundLAN2);
                            }
                            break;
                        case ConsoleKey.T:
                            Minsk.Clear();
                            break;
                        case ConsoleKey.Y:
                            Console.WriteLine("Please, enter hostname of LAN that you want to clear");
                            selectedLAN1 = Console.ReadLine();
     
                            if (Minsk.TryGetValue(selectedLAN1, out foundLAN))
                            {
                                foundLAN.Clear();
                            }
                            break;
                        case ConsoleKey.U:
                            Console.WriteLine("Please, enter hostname of desktop and LAN");
                            selectedHostname = Console.ReadLine();
                            selectedLAN1 = Console.ReadLine();
     
                            if (Minsk.TryGetValue(selectedLAN1, out foundLAN))
                            {
                                foundLAN.SetStaticIP(selectedHostname);
                            }
                            break;
                        case ConsoleKey.I:
                            Console.WriteLine("Please, enter hostname of desktop and LAN");
                            selectedHostname = Console.ReadLine();
                            selectedLAN1 = Console.ReadLine();
     
                            if (Minsk.TryGetValue(selectedLAN1, out foundLAN))
                            {
                                foundLAN.UnsetStaticIP(selectedHostname);
                            }
                            break;
                        case ConsoleKey.O:
                            Console.WriteLine("Please, enter hostnames of combined LAN's");
                            selectedLAN1 = Console.ReadLine();
                            selectedLAN2 = Console.ReadLine();
     
                            Minsk.Combine(selectedLAN1, selectedLAN2);
                            break;
                        case ConsoleKey.Escape:
                            exit = true;
                            Console.WriteLine(" Exit...");
                            break;
                    }
                }
            }
        }
    }

    
