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

![image](https://user-images.githubusercontent.com/65806232/215538456-5b2dace0-2be0-491f-98a6-d39a5dbf9e60.png)
![image](https://user-images.githubusercontent.com/65806232/215538559-9abee20e-46b6-42c4-8b24-bb5b119719f0.png)

6. Function update_item_name

![image](https://user-images.githubusercontent.com/65806232/215538690-2fa3b72f-338b-4eb7-b465-37c9366c6009.png)

7. Function update_item_qty

![image](https://user-images.githubusercontent.com/65806232/215538801-f9a10940-fcae-41e7-841e-9f6322a1cf63.png)

8. Function update_item_price

![image](https://user-images.githubusercontent.com/65806232/215538890-35eadf2c-4a7b-4d7e-8d12-7b173dc98361.png)

9. Function choose_delete

![image](https://user-images.githubusercontent.com/65806232/215539164-72b8982a-4577-4239-a5f9-57587c65191d.png)
![image](https://user-images.githubusercontent.com/65806232/215539193-3ef5a178-56d7-4e9a-a136-92ff88e77970.png)

10. Function delete_item

![image](https://user-images.githubusercontent.com/65806232/215539249-4c9856f2-c43a-4b64-bd8c-6acf00c94170.png)

11. Function reset_item

![image](https://user-images.githubusercontent.com/65806232/215539294-e4c7f3a1-6ff0-46da-bc3f-9c66c061f595.png)

12. Function check_item

![image](https://user-images.githubusercontent.com/65806232/215539363-5439dc20-0f03-4a1d-ac7e-5c17421f72fd.png)

13. Function total_price

![image](https://user-images.githubusercontent.com/65806232/215539418-0422b01e-a0f8-4c7c-94e0-21a2b51a268d.png)


## Conclusion
Program ini dapat memudahkan user dalam memasukkan barang yang ingin dibeli secara mandiri. Meski begitu, Interface program ini masih bisa dikembangkan lebih lanjut agar user lebih mudah dalam mengoperasikannya.
