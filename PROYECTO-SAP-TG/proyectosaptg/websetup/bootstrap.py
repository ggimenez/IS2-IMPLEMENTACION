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
#--------------------------------------------------------------------
        #Crea el permiso de 'ver_fase_todos'
        permiso9 = model.Permission()
        permiso9.cod_permiso = u'9'
        permiso9.permission_name = u'ver_fase_todos'
        permiso9.description = u'Permiso para ver fases de un proyecto'

        #Crea el permiso de 'crear_fase'
        permiso10 = model.Permission()
        permiso10.cod_permiso = u'10'
        permiso10.permission_name = u'crear_fase'
        permiso10.descripcion = u'Permiso para crear fase'

        #Crea el permiso de 'editar_fase'
        permiso11 = model.Permission()
        permiso11.cod_permiso = u'11'
        permiso11.permission_name = u'editar_fase'
        permiso11.descripcion = u'Permiso para editar fase'

        #Crea el permiso de 'eliminar_fase'
        permiso12 = model.Permission()
        permiso12.cod_permiso = u'12'
        permiso12.permission_name = u'eliminar_fase'
        permiso12.descripcion = u'Permiso para eliminar fase'
#--------------------------------------------------------------------
        #Crea el permiso de 'ver_item_todos'
        permiso13 = model.Permission()
        permiso13.cod_permiso = u'13'
        permiso13.permission_name = u'ver_item_todos'
        permiso13.descripcion = u'Permiso para ver items de un proyecto'

        #Crea el permiso de 'crear_item'
        permiso14 = model.Permission()
        permiso14.cod_permiso = u'14'
        permiso14.permission_name = u'crear_item'
        permiso14.descripcion = u'Permiso para crear items'

        #Crea el permiso de 'editar_item'
        permiso15 = model.Permission()
        permiso15.cod_permiso = u'15'
        permiso15.permission_name = u'editar_item'
        permiso15.descripcion = u'Permiso para editar item'

        #Crea el permiso de 'eliminar_item'
        permiso16 = model.Permission()
        permiso16.cod_permiso = u'16'
        permiso16.permission_name = u'eliminar_item'
        permiso16.descripcion = u'Permiso para eliminar item'
#--------------------------------------------------------------------
        #Crea el permiso de 'ver_LB_todos'
        permiso17 = model.Permission()
        permiso17.cod_permiso = u'17'
        permiso17.permission_name = u'ver_LB_todos'
        permiso17.descripcion = u'Permiso para ver LB de un proyecto'

        #Crea el permiso de 'crear_LB'
        permiso18 = model.Permission()
        permiso18.cod_permiso = u'18'
        permiso18.permission_name = u'crear_LB'
        permiso18.descripcion = u'Permiso para crear LB'

        #Crea el permiso de 'editar_LB'
        permiso19 = model.Permission()
        permiso19.cod_permiso = u'19'
        permiso19.permission_name = u'editar_LB'
        permiso19.descripcion = u'Permiso para editar LB'

        #Crea el permiso de 'eliminar_LB'
        permiso20 = model.Permission()
        permiso20.cod_permiso = u'20'
        permiso20.permission_name = u'eliminar_LB'
        permiso20.descripcion = u'Permiso para eliminar LB'
#--------------------------------------------------------------------
        #Crea el permiso de 'ver_relacion_todos'
        permiso21 = model.Permission()
        permiso21.cod_permiso = u'21'
        permiso21.permission_name = u'ver_relacion_todos'
        permiso21.descripcion = u'Permiso para ver relaciones de un proyecto'

        #Crea el permiso de 'crear_relacion'
        permiso22 = model.Permission()
        permiso22.cod_permiso = u'22'
        permiso22.permission_name = u'crear_relacion'
        permiso22.descripcion = u'Permiso para crear relacion'

        #Crea el permiso de 'editar_LB'
        permiso23 = model.Permission()
        permiso23.cod_permiso = u'23'
        permiso23.permission_name = u'editar_relacion'
        permiso23.descripcion = u'Permiso para editar relacion'

        #Crea el permiso de 'eliminar_relacion'
        permiso24 = model.Permission()
        permiso24.cod_permiso = u'24'
        permiso24.permission_name = u'eliminar_relacion'
        permiso24.descripcion = u'Permiso para eliminar relacion'
#----------------------------------------------------------------
        #Crea el permiso de 'revertir_item'
        permiso25 = model.Permission()
        permiso25.cod_permiso = u'25'
        permiso25.permission_name = u'revertir_item'
        permiso25.descripcion = u'Permiso para revertir items'

        #Crea el permiso de 'revivir_item'
        permiso26 = model.Permission()
        permiso26.cod_permiso = u'26'
        permiso26.permission_name = u'revivir_item'
        permiso26.descripcion = u'Permiso para revivir items'
        
        #Crea el permiso de 'editar_rol'
        permiso27 = model.Permission()
        permiso27.cod_permiso = u'27'
        permiso27.permission_name = u'editar_rol'
        permiso27.descripcion = u'Permiso para editar roles'
        
        #Crea el permiso de 'ver_rol'
        permiso28 = model.Permission()
        permiso28.cod_permiso = u'28'
        permiso28.permission_name = u'ver_rol'
        permiso28.descripcion = u'Permiso para ver roles'
        
        #Crea el permiso de 'aprobar_item'
        permiso29 = model.Permission()
        permiso29.cod_permiso = u'29'
        permiso29.permission_name = u'aprobar_item'
        permiso29.descripcion = u'Permiso para aprobar items'
        
        #Crea el permiso de 'aprobar_LB'
        permiso30 = model.Permission()
        permiso30.cod_permiso = u'30'
        permiso30.permission_name = u'aprobar_LB'
        permiso30.descripcion = u'Permiso para aprobar LBs'
        
        #Crea el permiso de 'crear_atributo'
        permiso31 = model.Permission()
        permiso31.cod_permiso = u'31'
        permiso31.permission_name = u'crear_atributo'
        permiso31.descripcion = u'Permiso para crear atributos'
        
        #Crea el permiso de 'editar_atributo'
        permiso32 = model.Permission()
        permiso32.cod_permiso = u'32'
        permiso32.permission_name = u'editar_atributo'
        permiso32.descripcion = u'Permiso para editar atributos'
#--------------------------------------------------------------------
        #Crea el permiso de 'ver_tipoItem_todos'
        permiso33 = model.Permission()
        permiso33.cod_permiso = u'33'
        permiso33.permission_name = u'ver_tipoItem_todos'
        permiso33.descripcion = u'Permiso para ver tipos de Items de un proyecto'

        #Crea el permiso de 'crear_tipoItem'
        permiso34 = model.Permission()
        permiso34.cod_permiso = u'34'
        permiso34.permission_name = u'crear_tipoItem'
        permiso34.descripcion = u'Permiso para crear tipoItem'

        #Crea el permiso de 'editar_tipoItem'
        permiso35 = model.Permission()
        permiso35.cod_permiso = u'35'
        permiso35.permission_name = u'editar_tipoItem'
        permiso35.descripcion = u'Permiso para editar tipoItem'

        #Crea el permiso de 'eliminar_tipoItem'
        permiso36 = model.Permission()
        permiso36.cod_permiso = u'36'
        permiso36.permission_name = u'eliminar_tipoItem'
        permiso36.descripcion = u'Permiso para eliminar tipoItem'


        ################### Root ################################
        model.DBSession.add(root)       #AGREGA EL USUARIO root AL MODELO
        Rolroot.users.append(root)      #AGREGA EL ROL Rolroot AL USUARIO ADMIN
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
        
        permiso9.groups.append(Rolroot)
        model.DBSession.add(permiso9)
        
        permiso10.groups.append(Rolroot)
        model.DBSession.add(permiso10)
        
        permiso11.groups.append(Rolroot)
        model.DBSession.add(permiso11)
        
        permiso12.groups.append(Rolroot)
        model.DBSession.add(permiso12)
        
        permiso13.groups.append(Rolroot)
        model.DBSession.add(permiso13)
        
        permiso14.groups.append(Rolroot)
        model.DBSession.add(permiso14)
        
        permiso15.groups.append(Rolroot)
        model.DBSession.add(permiso15)
        
        permiso16.groups.append(Rolroot)
        model.DBSession.add(permiso16)
        
        permiso17.groups.append(Rolroot)
        model.DBSession.add(permiso17)
        
        permiso18.groups.append(Rolroot)
        model.DBSession.add(permiso18)
        
        permiso19.groups.append(Rolroot)
        model.DBSession.add(permiso19)
        
        permiso20.groups.append(Rolroot)
        model.DBSession.add(permiso20)
        
        permiso21.groups.append(Rolroot)
        model.DBSession.add(permiso21)
        
        permiso22.groups.append(Rolroot)
        model.DBSession.add(permiso22)
        
        permiso23.groups.append(Rolroot)
        model.DBSession.add(permiso23)
        
        permiso24.groups.append(Rolroot)
        model.DBSession.add(permiso24)
        
        permiso25.groups.append(Rolroot)
        model.DBSession.add(permiso25)
        
        permiso26.groups.append(Rolroot)
        model.DBSession.add(permiso26)
        
        permiso27.groups.append(Rolroot)
        model.DBSession.add(permiso27)
        
        permiso28.groups.append(Rolroot)
        model.DBSession.add(permiso28)
        
        permiso29.groups.append(Rolroot)
        model.DBSession.add(permiso29)
        
        permiso30.groups.append(Rolroot)
        model.DBSession.add(permiso30)
        
        permiso31.groups.append(Rolroot)
        model.DBSession.add(permiso31)
        
        permiso32.groups.append(Rolroot)
        model.DBSession.add(permiso32)
        
        permiso33.groups.append(Rolroot)
        model.DBSession.add(permiso33)
        
        permiso34.groups.append(Rolroot)
        model.DBSession.add(permiso34)
        
        permiso35.groups.append(Rolroot)
        model.DBSession.add(permiso35)
        
        permiso36.groups.append(Rolroot)
        model.DBSession.add(permiso36)

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

        usermanager = model.User()
        usermanager.user_name = u'manager'
        usermanager.display_name = u'Example manager'
        usermanager.email_address = u'manager@somedomain.com'
        usermanager.password = u'managepass'

        model.DBSession.add(usermanager)

        RolManager = model.Group()
        RolManager.group_name = u'managers'
        RolManager.display_name = u'Managers Group'

        RolManager.users.append(usermanager)
        #agrega el rol g al usuario u

        model.DBSession.add(RolManager)
        #agrega el usuario g al modelo

        p = model.Permission()
        p.permission_name = u'manage'
        p.description = u'This permission give an administrative right to the bearer'
        #permiso p creado
        
        p.groups.append(RolManager)
        #agrega el permiso p al rol g
        p.groups.append(Rolroot)
        #agrega el permiso p al rol Rolroot
        model.DBSession.add(p)
        #agrega el permiso p al modelo
        #----------------------------------------------------------------------------
        permiso1.groups.append(RolManager) #AGREGA EL PERMISO 1 AL ROL
        model.DBSession.add(permiso1)   #AGREGA EL PERMISO AL AL MODELO

        permiso2.groups.append(RolManager)
        model.DBSession.add(permiso2)

        permiso3.groups.append(RolManager)
        model.DBSession.add(permiso3)

        permiso4.groups.append(RolManager)
        model.DBSession.add(permiso4)

        permiso5.groups.append(RolManager)
        model.DBSession.add(permiso5)

        permiso6.groups.append(RolManager)
        model.DBSession.add(permiso6)

        permiso8.groups.append(RolManager)
        model.DBSession.add(permiso8)
        
        permiso9.groups.append(RolManager)
        model.DBSession.add(permiso9)
        
        permiso10.groups.append(RolManager)
        model.DBSession.add(permiso10)
        
        permiso11.groups.append(RolManager)
        model.DBSession.add(permiso11)
        
        permiso12.groups.append(RolManager)
        model.DBSession.add(permiso12)
        
        permiso13.groups.append(RolManager)
        model.DBSession.add(permiso13)
        
        permiso14.groups.append(RolManager)
        model.DBSession.add(permiso14)
        
        permiso15.groups.append(RolManager)
        model.DBSession.add(permiso15)
        
        permiso16.groups.append(RolManager)
        model.DBSession.add(permiso16)
        
        permiso17.groups.append(RolManager)
        model.DBSession.add(permiso17)
        
        permiso18.groups.append(RolManager)
        model.DBSession.add(permiso18)
        
        permiso19.groups.append(RolManager)
        model.DBSession.add(permiso19)
        
        permiso20.groups.append(RolManager)
        model.DBSession.add(permiso20)
        
        permiso21.groups.append(RolManager)
        model.DBSession.add(permiso21)
        
        permiso22.groups.append(RolManager)
        model.DBSession.add(permiso22)
        
        permiso23.groups.append(RolManager)
        model.DBSession.add(permiso23)
        
        permiso24.groups.append(RolManager)
        model.DBSession.add(permiso24)
        
        permiso25.groups.append(RolManager)
        model.DBSession.add(permiso25)
        
        permiso26.groups.append(RolManager)
        model.DBSession.add(permiso26)
        
        permiso27.groups.append(RolManager)
        model.DBSession.add(permiso27)
        
        permiso28.groups.append(RolManager)
        model.DBSession.add(permiso28)
        
        permiso29.groups.append(RolManager)
        model.DBSession.add(permiso29)
        
        permiso30.groups.append(RolManager)
        model.DBSession.add(permiso30)
        
        permiso31.groups.append(RolManager)
        model.DBSession.add(permiso31)
        
        permiso32.groups.append(RolManager)
        model.DBSession.add(permiso32)
        
        permiso33.groups.append(RolManager)
        model.DBSession.add(permiso33)
        
        permiso34.groups.append(RolManager)
        model.DBSession.add(permiso34)
        
        permiso35.groups.append(RolManager)
        model.DBSession.add(permiso35)
        
        permiso36.groups.append(RolManager)
        model.DBSession.add(permiso36)
        #-----------------------------------------------------------------------------
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
