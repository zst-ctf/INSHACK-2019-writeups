# Dashlame - Part 1
Reverse

## Challenge 

Can you try our new password manager ? There's a free flag in every password archive created !

This challenge contains a second part in the Crypto category.

## Solution

We have a .pyc file, and we can decompile it to a Python source code using uncompyle6

	$ uncompyle6 dashlame.pyc > dashlame_decompiled.py

From the decompiled code, we seem to have the flag in a zlib bytestream.

	def createArchive():
	    archive_name = raw_input('Please enter your archive name: ')
	    passphraseA, passphraseB = get_random_passphrase()
	    print 'This is your passphrase :', passphraseA, passphraseB
	    print 'Please remember it or you will lose all your passwords.'
	    archive_filename = archive_name + '.db'
	    with open(archive_filename, 'wb') as (db_fd):
	        db_fd.write(zlib.decompress('x\x0b\x0e,IUH/M,Q0f`a`ddpPP````b\x18`\x04b\x164>!Ġ\x17y.\x03\x10Q0\n\x05\U0008c342%I9\x01E)p\x06scB\x02\\X<5\x18C\\#Bt\x14JS\x12sa\x0220W\x1370\x00(\x18\x05`\x08\x03#F\x16mYkhOH-I~O`В`"Z\x00&='))
	    encrypt_archive(archive_filename, passphraseA, passphraseB)
	    print 'Archive created successfully.'

However, the decompiler did not extract the bytes correctly, so let's retrieve it dynamically.

---

We know that `createArchive()` will produce a `.db` file, and then encrypt it to produce a `.dla` file. The `.db` file is deleted.

We can try to override `encrypt_archive()` to have no effect.

	$ python
	>>> import dashlame   ## import the pyc file

	>>> dashlame.encrypt_archive
	<function encrypt_archive at 0x105835410>

	>>> dashlame.encrypt_archive = lambda x, y, z: None

	>>> dashlame.createArchive()
	Please enter your archive name: test
	Getting random data from atmospheric noise and mouse movements..........
	This is your passphrase : condoled apparatchik
	Please remember it or you will lose all your passwords.
	Archive created successfully.

And we get the unencrypted file.

	$ strings test.db 
	SQLite format 3
	tablePasswordsPasswords
	CREATE TABLE Passwords(website TEXT, username TEXT, password TEXT)
	;website_exampleusernameINSA{Tis_bUt_a_SCr4tch}

## Flag

	INSA{Tis_bUt_a_SCr4tch}
