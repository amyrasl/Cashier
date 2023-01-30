import pandas as pd
from tabulate import tabulate

class Transaction:
  """Class dengan nama Transaction"""

  item_dict = {'Name':[],'Price':[],'Quantity':[],'Total':[]}

  def __init__(self):
    """
    Constructor Class Transaction

    Attributes:
      id_transaction (int): Input ID Transaksi
      menu (string): Input menu transaksi  
    """
    
    while True:
      try:
        id_transaction = int(input('Masukkan ID Transaksi: '))
        print(f"ID Transaksi Anda ialah {id_transaction}")
        break
      except ValueError:
        print('Format harus dalam bentuk angka!\n')
    
    menu = ''
    while(menu != '6'):
      print("\n==================================")
      print("============== MENU ==============")
      print("==================================")
      print("1. Tambahkan barang")
      print("2. Edit barang")
      print("3. Hapus barang")
      print("4. Lihat/Check transaksi")
      print("5. Lihat harga total")
      print("6. Keluar dari menu")
      menu = input('Ketik nomor menu: ')
      if menu == '1':
        self.add_item()
      elif menu == '2':
        self.edit_item()
      elif menu == '3':
        self.choose_delete()
      elif menu == '4':
        self.check_item()
      elif menu == '5':
        self.total_price()
      
  def add_item(self):
    """
    Fungsi untuk menambahkan barang ke dalam keranjang.

    Attributes:
      menu_add (string): Input untuk memilih melanjutkan penambahan barang atau tidak
      name (string): Input untuk nama barang
      price (int): Input untuk harga barang
      quantity (int): input untuk jumlah barang
      total_price (int): total harga barang
    """
    
    menu_add = ''
    while(menu_add!='y'):
      print("\n\n========PENAMBAHAN BARANG========")
      name = input('Masukkan nama :')
      while True:
        try:
          price = int(input('Masukkan harga: '))
          break
        except ValueError:
          print("Masukkan dalam format angka!")
          continue
      while True:
        try:
          quantity = int(input('Masukkan jumlah: '))
          break
        except ValueError:
          print("Masukkan dalam format angka!")
          continue
      
      total_price = quantity*price
      self.item_dict['Name'].append(name)
      self.item_dict['Price'].append(price)
      self.item_dict['Quantity'].append(quantity)
      self.item_dict['Total'].append(total_price)

      menu_add = input("\nApakah Anda ingin mengakhiri penambahan barang? (y/n): ")
      menu_add = menu_add.lower()

    print('\n\n=BARANG BERHASIL DIMASUKKAN KE DALAM KERANJANG=\n')
    df = pd.DataFrame(self.item_dict)
    print(tabulate(df,headers="keys",showindex=False))

  def edit_item(self):
    """
    Fungsi untuk meng-update barang yang ada di dalam keranjang.

    Attributes:
      menu_update (string): Input untuk memilih melanjutkan penambahan barang atau tidak
      name (string): Input untuk nama barang
      price (int): Input untuk harga barang
      quantity (int): input untuk jumlah barang
      total_price (int): total harga barang
      change (string): nama barang yang akan diubah
      idx (int): index list di dalam dictionary item 
    """
    
    def update_item_name(change,idx):
      """
      Fungsi untuk meng-update nama barang dan menampilkan barang yang telah diubah

      Parameter:
        change (string): nama barang yang akan diubah
        idx (int): index list di dalam dictionary item  

      Attributes:
        change_name (string): nama barang setelah diubah
      """
      
      change_name = input('Masukkan nama barang yang baru: ')
      self.item_dict['Name'][idx] = change_name
      df = pd.DataFrame(self.item_dict)
      print(f'Nama barang berhasil diubah!\n{tabulate(df,headers="keys",showindex=False)}')

    def update_item_qty(change,idx):
      """
        Fungsi untuk meng-update jumlah barang dan menampilkan barang yang telah diubah

        Parameter:
          change (string): nama barang yang akan diubah
          idx (int): index list di dalam dictionary item  

        Attributes:
          change_quantity (int): jumlah barang setelah diubah
      """
      
      while True:
        try:
          change_quantity = int(input('Masukkan jumlah barang yang baru: '))
          self.item_dict['Quantity'][idx] = change_quantity
          self.item_dict['Total'][idx] = self.item_dict['Quantity'][idx]*self.item_dict['Price'][idx]
          
          df = pd.DataFrame(self.item_dict)
          print(f'Jumlah barang berhasil diubah!\n{tabulate(df,headers="keys",showindex=False)}')
          break
        except ValueError:
          print("Masukkan dalam bentuk angka!")

    def update_item_price(change,idx):
      """
        Fungsi untuk meng-update harga barang dan menampilkan barang yang telah diubah

        Parameter:
          change (string): nama barang yang akan diubah
          idx (int): index list di dalam dictionary item  

        Attributes:
          change_price (int): jumlah barang setelah diubah
      """
      
      while True:
        try:
          change_price = int(input('Masukkan harga barang yang baru: '))
          self.item_dict['Price'][idx] = change_price
          self.item_dict['Total'][idx] = self.item_dict['Quantity'][idx]*self.item_dict['Price'][idx]
          
          df = pd.DataFrame(self.item_dict)
          print(f'Harga barang berhasil diubah!\n{tabulate(df,headers="keys",showindex=False)}')
          break
          
        except ValueError:
          print("Masukkan dalam bentuk angka!") 

    if (all(map(lambda x: x == [], self.item_dict.values()))):
      print("\nBelum ada barang dalam keranjang!")
    else:
      while True:
        print('\n========================================================')
        print('======================= UPDATE =========================')
        print('========================================================')
        try:
          change = input('Masukkan barang yang ingin diubah: ')
          idx = self.item_dict['Name'].index(change)
          print('1. Update nama barang\n2. Update kuantitas barang\n3. Update harga barang')
          menu_update = input('Masukkan angka menu: ')
          if(menu_update == '1'):
            update_item_name(change,idx)
          if(menu_update == '2'):
            update_item_qty(change,idx)
          if(menu_update == '3'):
            update_item_price(change,idx)
          break
        except ValueError:
          print("Tidak ada barang dalam keranjang!\n")

  def choose_delete(self):
    """
    Fungsi untuk menghapus barang yang ada di dalam keranjang.

    Attributes:
      menu_delete (string): Input untuk memilih melanjutkan penambahan barang atau tidak
    """
    
    def delete_item(self):
      """
      Fungsi untuk menghapus satu barang

      Attributes:
        delete_name (string): Input nama barang yang ingin dihapus
        idx (int): index list di dalam dictionary item
      """
      
      while True:
        try:
          delete_name = input('Masukkan nama barang yang ingin dihapus: ')
          idx = self.item_dict['Name'].index(delete_name)
          for key in list(self.item_dict.keys()):
            del(self.item_dict[key][idx])
          df = pd.DataFrame(self.item_dict)
          print(f'Berhasil dihapus!\n {tabulate(df,headers="keys",showindex=False)}')
          break
        except ValueError:
          print("Tidak ada barang dalam keranjang!\n")

    def reset_item(self):
      """Fungsi untuk menghapus transaksi"""

      self.item_dict.clear()
      print('Semua barang berhasil dihapus!')

    if (all(map(lambda x: x == [], self.item_dict.values()))):
      print("\nBelum ada barang dalam keranjang!")
    else:
      print('============================================')
      print('===============HAPUS TRANSAKSI==============')
      print('============================================')
      print('1. Hapus satu barang')
      print('2. Hapus semua barang')
      menu_delete = input('Masukkan angka menu: ')
      if(menu_delete == '1'):
        delete_item(self)
      if(menu_delete == '2'):
        reset_item(self)

  def check_item(self):
    """Check barang apakah terdapat error"""
    
    if(all(map(lambda x: x == [], self.item_dict.values()))):
      print("\bBelum ada barang di keranjang!")
    else:
      print("\nData telah diisi dengan benar!")
      df = pd.DataFrame(self.item_dict)
      print(tabulate(df,headers="keys",showindex=False))

  def total_price(self):
    """
    Menampilkan total harga yang perlu dibayar setelah diakumulasikan dengan diskon
    
    Attributes:
      total_harga_diskon = total harga yang diakumulasikan dengan diskon
    """
    
    if (all(map(lambda x: x == [], self.item_dict.values()))):
      print("\nBelum ada barang dalam keranjang!")
    else:
      print("\n\n===== Berikut barang yang akan dibeli ======\n")
      print(tabulate(pd.DataFrame(self.item_dict),headers="keys",showindex=False))
      print("\n")

      total_harga_diskon = 0

      for value in list(self.item_dict.get('Total')):
        total_harga_diskon += value
      if(total_harga_diskon > 500000):
        print(f"Totalnya ialah Rp.{int(total_harga_diskon)}\nMENDAPATKAN DISKON 10%")
        total_harga_diskon -= 0.1*total_harga_diskon
      elif(total_harga_diskon > 300000):
        print(f"Totalnya ialah Rp.{int(total_harga_diskon)}, MENDAPATKAN DISKON 8%")
        total_harga_diskon -= 0.08*total_harga_diskon
      elif(total_harga_diskon > 200000):
        print(f"Totalnya ialah Rp.{int(total_harga_diskon)}, MENDAPATKAN DISKON 5%")
        total_harga_diskon -= 0.05*total_harga_diskon

      print(f"Total biaya yang perlu dibayar adalah Rp.{int(total_harga_diskon)}")
