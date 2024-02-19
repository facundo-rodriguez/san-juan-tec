


from sqlalchemy import Column

from imports import *

from envio_email import enviar_email




class Base(MappedAsDataclass, DeclarativeBase):
    pass


class Cliente(Base, order=True):
    __tablename__ = "cliente"

    
    sort_index:Mapped[date]=mapped_column(init=False, repr=False)
    id_cliente:Mapped[int]= mapped_column(init=False, primary_key=True)
    dni:Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    nombre:Mapped[str] = mapped_column(String(255), nullable=False) 
    apellido:Mapped[str] = mapped_column(String(255),nullable=False)
    nacimiento:Mapped[date]=mapped_column(Date,nullable=False)
    correo_electronico:Mapped[Optional[str]]=mapped_column(String(255),nullable=True,init=False)
    
   
    ordenes:Mapped[List["Orden"]]= relationship("Orden",cascade="all", back_populates="cliente",lazy='select')


    def __post_init__(self):

        self.sort_index=self.nacimiento
        

    def __str__(self) -> str:
        return f"dni: {self.dni}, nombre: {self.nombre}, apellido: {self.apellido}, nacimiento: {self.nacimiento}"


    @classmethod
    def registrar_cliente(cls,session):
        
        try:
            
            dni=input("Ingrese su DNI: ")
            nombre=input("Ingrese su nombre: ")
            apellido=input("Ingrese su apellido: ")
            
            nacimiento=input("Ingrese su fecha de nacimiento en formato dia-mes-año: ")
            nacimiento=datetime.strptime(nacimiento, "%d-%m-%Y").date()
        
            correo_electronico=input("Ingrese su correo electronico: ")

            periodo=date.today()-nacimiento
            edad=periodo.days//365
        
            if(date.today()>=nacimiento):
                
                if(edad>=18):
                    
                    cliente=cls(dni=dni,nombre=nombre,apellido=apellido,nacimiento=nacimiento,ordenes=[])
                    cliente.correo_electronico=correo_electronico
                    
                    session.add(cliente)
                    session.commit()

                    print("se ha registrado al cliente correctamente")
                else:
                    
                    print("su edad es: ", edad)
                    print("debe ser mayor de edad para poder registrarlo")
            
            else:
                print("la fecha de nacimiento debe ser anterior a la actual")
        
        except Exception as e:
            print("error")
            print(e)


    @classmethod
    def buscar_cliente(cls,session):

       dni=input("ingrese el dni del cliente a buscar: ")
       cliente=session.query(cls).filter_by(dni=dni).first() 

       return cliente


    @classmethod
    def listar_clientes(cls,opcion,session):
        
        clientes=session.query(cls)
        
        if(opcion==1):
            for i in clientes:
                print(i)
        
        else:

            destinatario=input("ingrese el correo del destinatario: ")

            with open("archivo.txt","w") as archivo:

                for i in clientes:
                    
                    archivo.write(str(i)+" \n")
            
            enviar_email(
                            smtp_server = "smtp.gmail.com",
                            smtp_port = 587,
                            smtp_user = "jazminrocio1998@gmail.com",  
                            smtp_pass = "mqcr cmjx lgoo rmso",
                            from_email = "jazminrocio1998@gmail.com",
                            to_email = destinatario,
                            subject = "Probando",
                            message = "en el archivo adjunto esta la lista de clientes."
                        )
            



        





class Orden(Base):
       
    __tablename__ = 'orden'

    sort_index:Mapped[date]=mapped_column(init=False, repr=False)
    id_orden: Mapped[int] = mapped_column( init=False, primary_key=True)
    fk_cliente: Mapped[int] = mapped_column(  ForeignKey('cliente.id_cliente'),init=False,nullable=False)
    fecha: Mapped[datetime]
       
    cliente:Mapped[Cliente]=relationship("Cliente",back_populates='ordenes') 

    productos:Mapped[List["OrdenProducto"]]= relationship(cascade="all", back_populates="orden",lazy='select')
    

    def __post_init__(self):

        self.sort_index=self.fecha


    def __str__(self) -> str:
        return f"id_orden: {self.id_orden}, fecha: {self.fecha}, cliente: {self.cliente.nombre}"


    @classmethod
    def crear_orden(cls,session):

        cliente=Cliente.buscar_cliente(session)

        if(cliente):
                    
            orden=Orden(cliente=cliente, productos=[], fecha=date.today())
            session.add(orden)
        
            while True:

                print("busque el producto que quiere ingresar a la orden de compra del cliente ", cliente.nombre, "",cliente.apellido) 
                producto=Producto.buscar_producto(session)

                if(producto):

                    cantidad=int(input("Ingrese la cantidad vendida del producto: "))

                    if(producto.stock>=cantidad):
            
                        
                        producto.stock-=cantidad
                        
                        ordenProducto=OrdenProducto(orden=orden,producto=producto)
                        ordenProducto.cantidad=cantidad
                        ordenProducto.calcular_monto()
                    
                        orden.productos.append(ordenProducto)
                        cliente.ordenes.append(orden)
                        
                         
                    else:
                        print("stock insuficiente :/")
            
                else:
                    print("no se encontro el producto")


                num=int(input("quiere ingresar otro producto a la orden de compra del cliente? 1 para si, 2 para no: "))
                if(num!=1):
                    break

            session.commit() 
            print("orden de compra registrada con exito")

        else:
            print("no se encontro el cliente")






class  Producto(Base) :

    __tablename__="productos"

    sort_index:Mapped[int]=mapped_column(init=False, repr=False)
    id_producto:Mapped[int]=mapped_column( init=False,primary_key=True,nullable=False,autoincrement=True)
    codigo:Mapped[str]=mapped_column(String(50),nullable=False,unique=True)
    nombre:Mapped[str]=mapped_column(String(100),nullable=False)
    "precio (float que debe ser el precio cargado más el impuesto)"
    precio:Mapped[float]= mapped_column(Float(precision=10,asdecimal=True),nullable=False)
    stock:Mapped[int]= mapped_column(Integer,nullable=False)
    type:Mapped[str]= mapped_column(String(100),init=False, nullable=False)
    fecha_alta:Mapped[DateTime]= mapped_column(DateTime,init=False, nullable=False, default=func.now())

    ordenes:Mapped[List["OrdenProducto"]] = relationship("OrdenProducto", back_populates="producto",lazy='select')


    __mapper_args__ = { 
        "polymorphic_identity": "producto",
        "polymorphic_on": "type"
    }

    def __post_init__(self):

        self.sort_index=self.precio


    def __str__(self) -> str:
        return f"id producto: {self.id_producto}, codigo:{self.codigo}, nombre: {self.nombre}, precio: {self.precio: .2f}, stock: {self.stock}, fecha de alta: {self.fecha_alta}, tipo: {self.type}"
      

    @classmethod
    def registrar_producto(cls,session):
        
        
        codigo=input("ingrese el codigo de producto: ")
        nombre=input("ingrese el nombre del producto: ")
        stock=int(input("ingrese el stock del producto: "))
        precio=float(input("ingrese el precio del producto: "))

        producto= cls(codigo=codigo,nombre=nombre, stock=stock, precio=precio,ordenes=[] ) #, fecha_alta=datetime(2020,1,1)
        session.add(producto)
        session.commit()
        print("producto registrado")



    @classmethod
    def listar_productos(cls,session):

        productos=session.query(cls).order_by(cls.precio)
        for producto in productos:
            print(producto)
    

    @classmethod 
    def buscar_producto(cls,session):
        
        codigo=input("ingrese el codigo de producto: ")
        producto=session.query(cls).filter(cls.codigo==codigo).first()

        return producto




class OrdenProducto(Base):
    
    __tablename__ = "orden_productos"

    id = Column(Integer, primary_key=True)
    fk_orden= Column(Integer, ForeignKey("orden.id_orden"), nullable=False)
    fk_producto= Column(Integer, ForeignKey("productos.id_producto"), nullable=False)
    cantidad = Column(Integer, nullable=False)
    monto=Column(Float, nullable=False)

    # Relación muchos a uno con la clase Orden
    orden:Mapped["Orden"]= relationship(back_populates="productos")

    # Relación muchos a uno con la clase Producto
    producto:Mapped["Producto"]= relationship(back_populates="ordenes")
    
    
    def __str__(self) -> str:
        return f"id_orden: {self.orden.id_orden}, codigo producto: {self.producto.codigo}, nombre producto: {self.producto.nombre}, cantidad vendida: {self.cantidad} "

    
    def calcular_monto(self):
        self.monto = self.cantidad * self.producto.precio


        