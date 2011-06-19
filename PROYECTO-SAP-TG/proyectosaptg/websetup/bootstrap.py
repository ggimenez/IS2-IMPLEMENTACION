# -*- coding: utf-8 -*-
"""Setup the PROYECTO-SAP-TG application"""

import logging
from tg import config
from proyectosaptg import model

import transaction


def bootstrap(command, conf, vars):
    """Place any commands to setup proyectosaptg here"""

    # <websetup.bootstrap.before.auth
    from sqlalchemy.exc import IntegrityError
    try:
        #####USUARIOS#####
        root = model.User()
        root.cod_usuario = u'root'
        root.user_name = u'root'
        root.email_address = u'root@mail.com'
        root.password = u'root'
        root.nombre = u'root'

        prueba = model.User()
        prueba.cod_usuario = u'prueba'
        prueba.user_name = u'prueba'
        prueba.email_address = u'prueba@mail.com'
        prueba.password = u'prueba'
        prueba.nombre = u'prueba'

        toy = model.User()
        toy.cod_usuario = u'toy'
        toy.user_name = u'toy'
        toy.email_address = u'toy@mail.com'
        toy.password = u'toy'
        toy.nombre = u'toy'

        #####ROLES#####

        #Crea el rol de root
        Rolroot = model.Group()
        Rolroot.cod_rol = u'Rroot'
        Rolroot.group_name = u'Root'
        Rolroot.descripcion = u'Grupo de roots'

        #Crea el rol de prueba
        Rolprueba = model.Group()
        Rolprueba.cod_rol = u'Rprueba'
        Rolprueba.group_name = u'Prueba'
        Rolprueba.descripcion = u'Grupo de pruebas'

        #Crea el rol de toys    
        Roltoy = model.Group()
        Roltoy.cod_rol = u'Rtoy'
        Roltoy.group_name = u'Toy'
        Roltoy.descripcion = u'Grupo de juguete'


        #####PERMISOS#####

        #Crea el permiso de 'ver_usuario_todos'
        permiso1 = model.Permission()
        permiso1.cod_permiso = u'1'
        permiso1.permission_name = u'ver_usuario_todos'
        permiso1.descripcion = u'Permiso para ver usuario'

        #Crea el permiso de 'crear_usuario'
        permiso2 = model.Permission()
        permiso2.cod_permiso = u'2'
        permiso2.permission_name = u'crear_usuario'
        permiso2.descripcion = u'Permiso para crear usuario'

        permiso3 = model.Permission()
        permiso3.cod_permiso = u'3'
        permiso3.permission_name = u'editar_usuario'
        permiso3.descripcion = u'Permiso para editar usuario'

        #Crea el permiso de 'eliminar_usuario'
        permiso4 = model.Permission()
        permiso4.cod_permiso = u'4'
        permiso4.permission_name = u'eliminar_usuario'
        permiso4.descripcion = u'Permiso para eliminar usuario'

        #Crea el permiso de 'ver_proyecto_todos'
        permiso5 = model.Permission()
        permiso5.cod_permiso = u'5'
        permiso5.permission_name = u'ver_proyecto_todos'
        permiso5.descripcion = u'Permiso para ver proyecto'

        #Crea el permiso de 'crear_proyecto'
        permiso6 = model.Permission()
        permiso6.cod_permiso = u'6'
        permiso6.permission_name = u'crear_proyecto'
        permiso6.descripcion = u'Permiso para crear proyecto'

        #Crea el permiso de 'editar_proyecto'
        permiso7 = model.Permission()
        permiso7.cod_permiso = u'7'
        permiso7.permission_name = u'editar_proyecto'
        permiso7.descripcion = u'Permiso para editar proyecto'

        #Crea el permiso de 'eliminar_proyecto'
        permiso8 = model.Permission()
        permiso8.cod_permiso = u'8'
        permiso8.permission_name = u'eliminar_proyecto'
        permiso8.descripcion = u'Permiso para eliminar proyecto'


        ################### Root ################################
        model.DBSession.add(root)       #AGREGA EL USUARIO ADMIN AL MODELO
        Rolroot.users.append(root)      #AGREGA EL ROL ADMINISTRADOR AL USUARIO ADMIN
        model.DBSession.add(Rolroot)    #AGREGA EL ROL AL MODELO

        permiso1.groups.append(Rolroot) #AGREGA EL PERMISO 1 AL ROL
        model.DBSession.add(permiso1)   #AGREGA EL PERMISO AL AL MODELO

        permiso2.groups.append(Rolroot)
        model.DBSession.add(permiso2)

        permiso3.groups.append(Rolroot)
        model.DBSession.add(permiso3)

        permiso4.groups.append(Rolroot)
        model.DBSession.add(permiso4)

        permiso5.groups.append(Rolroot)
        model.DBSession.add(permiso5)

        permiso6.groups.append(Rolroot)
        model.DBSession.add(permiso6)

        permiso8.groups.append(Rolroot)
        model.DBSession.add(permiso8)


        ################### Prueba ################################
        model.DBSession.add(prueba)         #AGREGA EL USUARIO LID AL MODELO
        Rolprueba.users.append(prueba)      #AGREGA EL ROL LIDER AL USUARIO LID
        model.DBSession.add(Rolprueba)      #AGREGA EL ROL AL MODELO

        permiso5.groups.append(Rolprueba)   #AGREGA EL PERMISO 5 AL ROL DE LIDER
        model.DBSession.add(permiso5)       #AGREGA EL PERMISO AL MODELO

        permiso7.groups.append(Rolprueba)
        model.DBSession.add(permiso7)

        #################### Toy #####################
        model.DBSession.add(toy)        #AGREGA EL USUARIO ADMIN AL MODELO
        Roltoy.users.append(toy)        #AGREGA EL ROL ADMINISTRADOR AL USUARIO ADMIN
        model.DBSession.add(Roltoy)

        u = model.User()
        u.user_name = u'manager'
        u.display_name = u'Example manager'
        u.email_address = u'manager@somedomain.com'
        u.password = u'managepass'

        model.DBSession.add(u)

        g = model.Group()
        g.group_name = u'managers'
        g.display_name = u'Managers Group'

        g.users.append(u)

        model.DBSession.add(g)

        p = model.Permission()
        p.permission_name = u'manage'
        p.description = u'This permission give an administrative right to the bearer'
        p.groups.append(g)
        p.groups.append(Rolroot)

        model.DBSession.add(p)

        u1 = model.User()
        u1.user_name = u'editor'
        u1.display_name = u'Example editor'
        u1.email_address = u'editor@somedomain.com'
        u1.password = u'editpass'

        model.DBSession.add(u1)
        model.DBSession.flush()
        transaction.commit()
    except IntegrityError:
        print 'Warning, there was a problem adding your auth data, it may have already been added:'
        import traceback
        print traceback.format_exc()
        transaction.abort()
        print 'Continuing with bootstrapping...'
        

    # <websetup.bootstrap.after.auth>
