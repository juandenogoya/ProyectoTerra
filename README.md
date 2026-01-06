# 🏪 Terra Retail - Sistema de Gestión Comercial

Sistema de gestión comercial para retail de indumentaria y calzado, desarrollado con Django.

## 🎯 Características

- **Gestión de Productos**: Control de inventario con tallas, colores y stock
- **Punto de Venta (POS)**: Sistema de ventas ágil y moderno
- **Gestión de Clientes**: Base de datos completa de clientes
- **Proveedores y Compras**: Control de órdenes y proveedores
- **Reportes y Analytics**: Visualización de ventas y stock
- **UI Moderna**: Interfaz responsive con Tailwind CSS

## 🚀 Stack Tecnológico

- **Backend**: Django 5.0
- **Frontend**: HTMX + Alpine.js + Tailwind CSS
- **Base de datos**: PostgreSQL (producción) / SQLite (desarrollo)
- **Cache**: Redis (opcional)

## 📋 Prerequisitos

- Python 3.11+
- pip
- virtualenv (recomendado)

## 🛠️ Instalación

### 1. Clonar el repositorio
```bash
git clone <repository-url>
cd ProyectoTerra
```

### 2. Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

### 5. Ejecutar migraciones
```bash
python manage.py migrate
```

### 6. Crear superusuario
```bash
python manage.py createsuperuser
```

### 7. Iniciar servidor
```bash
python manage.py runserver
```

Acceder a: http://localhost:8000

## 📁 Estructura del Proyecto

```
ProyectoTerra/
├── backend/                    # Proyecto Django principal
│   ├── config/                # Configuración del proyecto
│   ├── apps/                  # Aplicaciones Django
│   │   ├── clientes/         # Gestión de clientes
│   │   ├── productos/        # Catálogo de productos
│   │   ├── inventario/       # Control de stock
│   │   ├── ventas/           # POS y facturación
│   │   ├── compras/          # Proveedores y órdenes
│   │   ├── reportes/         # Analytics y reportes
│   │   └── usuarios/         # Autenticación
│   ├── static/               # CSS, JS, imágenes
│   └── templates/            # Plantillas HTML
├── requirements.txt          # Dependencias Python
├── .env.example             # Ejemplo de variables de entorno
├── .gitignore              # Archivos ignorados por git
└── README.md               # Este archivo
```

## 🔧 Comandos Útiles

```bash
# Crear nueva app
python manage.py startapp nombre_app

# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Recopilar archivos estáticos
python manage.py collectstatic

# Ejecutar tests
python manage.py test
```

## 📦 Módulos Principales

### Clientes
- Registro y gestión de clientes
- Historial de compras
- Preferencias y notas

### Productos
- Catálogo con categorías
- Variantes (tallas, colores)
- Imágenes y descripciones
- Precios y descuentos

### Inventario
- Control de stock en tiempo real
- Alertas de stock mínimo
- Movimientos de inventario
- Ajustes y transferencias

### Ventas
- Punto de venta (POS)
- Facturación
- Devoluciones
- Métodos de pago

### Reportes
- Dashboard de ventas
- Top productos
- Análisis de inventario
- Reportes personalizados

## 🔐 Seguridad

- Variables sensibles en `.env` (no en código)
- SECRET_KEY segura
- CSRF protection activado
- Autenticación y permisos por roles

## 📝 TODO

- [ ] Configurar proyecto Django base
- [ ] Implementar módulo de productos
- [ ] Desarrollar POS
- [ ] Sistema de reportes
- [ ] Integración de pagos
- [ ] App móvil (futuro)

## 👥 Contribución

Proyecto en desarrollo.

## 📄 Licencia

Uso privado - Todos los derechos reservados.

---

Desarrollado con ❤️ para Terra Retail
