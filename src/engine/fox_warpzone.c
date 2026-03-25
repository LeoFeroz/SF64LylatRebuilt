#include "global.h"
#include "assets/ast_warp_zone.h"

void WarpZone_Skybox_Init(void) {
    ActorCutscene2* WpSkyEff = &gBosses[4];

    Actor_Initialize(WpSkyEff);
    WpSkyEff->obj.status = OBJ_INIT;
    WpSkyEff->obj.id = OBJ_ACTOR_CUTSCENE2;

    WpSkyEff->obj.pos.x = 0.0f;
    WpSkyEff->obj.pos.y = 0.0f;
    WpSkyEff->obj.pos.z = gPlayer->pos.z;

    WpSkyEff->animFrame = ACTOR_CS_WRP_SKYBOX;
    Object_SetInfo(&WpSkyEff->info, WpSkyEff->obj.id);
}
