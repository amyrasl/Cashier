# Super Cashier

## Latar Belakang
Super Cashier merupakan sistem kasir yang mampu membuat user memesan barang secara self-service. Sistem digunakan agar user dapat mengelola sendiri barang apa saja yang ingin dibeli.

## Program Objectives
 - Membuat ID Transaksi
 - Menambahkan barang ke dalam keranjang
 - Memperbarui nama, jumlah, dan harga barang di dalam keranjang
 - Menghapus barang di dalam keranjang
 - Reset semua barang dalam keranjang
 - Mengecek error dalam keranjang
 - Menampilkan harga total barang dengan diskon

## Workflow
 ### Add Item
 1. User diminta untuk memasukkan nama barang
 2. User diminta untuk memasukkan harga barang
 3. User diminta untuk memasukkan jumlah barang
 4. User akan ditanya apakah ingin mengakhiri penambahan barang, jika iya maka ketikkan 'y' dan 'n' jika tidak
 5. Akan ditampilkan kalimat 'Barang berhasil dimasukkan ke dalam keranjang

 ### Update Item
 1. User diminta untuk memasukkan nama barang yang ingin diubah
 2. User akan ditanya apakah ingin mengubah nama, harga, atau jumlah barang
 3. Jika user ingin mengubah nama barang sesuai dengan input nama barang yang ingin diubah, maka user akan diminta memasukkan nama barang yang baru
 4. Jika user ingin mengubah harga barang sesuai dengan input nama barang yang ingin diubah, maka user akan diminta memasukkan harga barang yang baru
 5. Jika user ingin mengubah jumlah barang sesuai dengan input nama barang yang ingin diubah, maka user akan diminta memasukkan jumlah barang yang baru

 ### Delete Item
 1. User ditanya apakah ingin menghapus satu barang atau ingin me-reset seluruh barang pada keranjang
 2. Jika user ingin menghapus satu barang, maka user akan diminta memasukkan nama barang yang ingin dihapus
 3. Jika user ingin me-reset seluruh barang, maka sistem akan menghapus seluruh transaksi dan menampilkan 'Transaksi berhasil dihapus'

 ### Check Item
 1. Sistem akan mengecek apakah terdapat barang dalam keranjang, jika tidak, sistem akan menampilkan 'Belum ada barang di dalam keranjang'
 2. Jika di dalam keranjang sudah diisi dengan benar, maka akan ditampilkan 'Data sudah diisi dengan benar' dan ditampilkan seluruh barang pada keranjang

 ### Total Price
 1. Sistem akan mengecek apakah terdapat barang dalam keranjang, jika tidak, sistem akan menampilkan 'Belum ada barang di dalam keranjang'
 2. Sistem akan menampilkan barang yang telah dibeli dengan total biaya yang sudah dikalkulasikan dengan diskon


## Demonstrasi Code
1. Script Main.py

```ruby
import transaction

trnsct_123 = transaction.Transaction()
```

2. Script Transaction.py
Berisikan Class Transaction yang berisikan variabel dictionary sebagai cart

```ruby
class Transaction:
  """Class dengan nama Transaction"""

  item_dict = {'Name':[],'Price':[],'Quantity':[],'Total':[]}
```

3. Constructor init
Terdapat menu yang dapat user pilih sebagai opsi memesan barang. Pertanyaan menu akan terus berulang hingga user keluar dari menu dengan menekan angka 6

```ruby
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
```

4. Function add_item

```ruby
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
```

5. Function edit_item

```ruby
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
```

6. Function update_item_name

```ruby
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
      print(f'Nama barang berhasil diubah! {self.item_dict} \n\n')
```

7. Function update_item_qty

```ruby
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
          
          print(f'Jumlah barang berhasil diubah! {self.item_dict} \n\n')
          break
        except ValueError:
          print("Masukkan dalam bentuk angka!")
```

8. Function update_item_price

```ruby
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
          
          print(f'Harga barang berhasil diubah! {self.item_dict} \n\n')
          break
          
        except ValueError:
          print("Masukkan dalam bentuk angka!") 
```

9. Function choose_delete

```ruby
  def choose_delete(self):
    """
    Fungsi untuk menghapus barang yang ada di dalam keranjang.
    Attributes:
      menu_delete (string): Input untuk memilih melanjutkan penambahan barang atau tidak
    """
    
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
```

10. Function delete_item

```ruby
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
          print(f'Berhasil dihapus! {tabulate(df,headers="keys",showindex=False)}')
          break
        except ValueError:
          print("Tidak ada barang dalam keranjang!\n")
```

11. Function reset_item

```ruby
    def reset_item(self):
      """Fungsi untuk menghapus transaksi"""

      self.item_dict.clear()
      print('Semua barang berhasil dihapus!')
```

12. Function check_item

```ruby
  def check_item(self):
    """Check barang apakah terdapat error"""
    
    if(all(map(lambda x: x == [], self.item_dict.values()))):
      print("\bBelum ada barang di keranjang!")
    else:
      print("\nData telah diisi dengan benar!")
      df = pd.DataFrame(self.item_dict)
      print(tabulate(df,headers="keys",showindex=False))

```

13. Function total_price

```ruby
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
```

##Test Case
1. Test Case1: Penambahan barang

![image](https://user-images.githubusercontent.com/65806232/215543723-70d1e12d-61ee-4e74-8ccf-e27a2ae23a4a.png)

2. Test Case2: Delete item

![image](https://user-images.githubusercontent.com/65806232/215545629-71bd382d-7697-4857-a0e2-f7d72ecc8af1.png)

3. Test Case3: Reset item

![image](https://user-images.githubusercontent.com/65806232/215546239-5e7bf95b-917d-4347-b108-4bd6031bc0cf.png)

4. Test Case4: Total item

![image](https://user-images.githubusercontent.com/65806232/215547101-eda2b8e9-3d9a-48d1-a507-82fc180e72b6.png)

## Conclusion
Program ini dapat memudahkan user dalam memasukkan barang yang ingin dibeli secara mandiri. Meski begitu, Interface program ini masih bisa dikembangkan lebih lanjut agar user lebih mudah dalam mengoperasikannya.
