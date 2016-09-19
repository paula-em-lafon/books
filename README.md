# Books
Aplicación sencilla para agregar y quitar "libros", "autores" y "editoriales"


## Prerequisitos
+ [Oracle's VirtualBox](https://www.virtualbox.org/)
+ [Vagrant](http://www.vagrantup.com/)
+ [Python](http://www.python.org/)
+ [Fabric](http://www.fabfile.org/)
+ [fabutils](https://github.com/vinco/fabutils)


## Uso

1. Crear máquina virtual

    ```bash
    $ vagrant up
    ```
2. redirigir dominio a
    ```bash
    # /etc/hosts
    192.168.33.2  http://books.local/
    ```

3. Hacer bootstrap para crear las partes de la máquina virtual
    
    ```bash
    $ fab environment:vagrant bootstrap
    ```

4. Correr el servidor de desarrollo
    
    ```bash
    $ fab environment:vagrant runserver
    ```
