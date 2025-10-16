/*******************************************************************************************
 * CirAni - Circuit Animation Demo
 * A simple raylib example demonstrating electron movement in a circuit
 *******************************************************************************************/

#include "raylib.h"
#include <stdio.h>
#include <math.h>

#define SCREEN_WIDTH 800
#define SCREEN_HEIGHT 600

typedef struct {
    Vector2 position;
    Vector2 velocity;
    float radius;
    Color color;
} Electron;

int main(void)
{
    InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, "CirAni - Circuit Animation");
    SetTargetFPS(60);

    Electron electron = {
        .position = { SCREEN_WIDTH / 2.0f, SCREEN_HEIGHT / 2.0f },
        .velocity = { 2.0f, 1.5f },
        .radius = 10.0f,
        .color = BLUE
    };

    Vector2 wireStart = { 100, SCREEN_HEIGHT / 2.0f };
    Vector2 wireEnd = { SCREEN_WIDTH - 100, SCREEN_HEIGHT / 2.0f };

    float animationTime = 0.0f;

    printf("CirAni started successfully!\n");
    printf("Press ESC to exit\n");

    while (!WindowShouldClose())
    {
        // Update
        animationTime += GetFrameTime();

        // Move electron along the wire
        float t = (sin(animationTime) + 1.0f) / 2.0f;
        electron.position.x = wireStart.x + (wireEnd.x - wireStart.x) * t;
        electron.position.y = wireStart.y + sin(animationTime * 3.0f) * 20.0f;

        // Change color based on time
        electron.color = (Color){
            (unsigned char)(128 + sin(animationTime) * 127),
            (unsigned char)(128 + cos(animationTime * 1.5f) * 127),
            255,
            255
        };

        // Draw
        BeginDrawing();

            ClearBackground(RAYWHITE);

            DrawText("CirAni - Circuit Animation Demo", 10, 10, 20, DARKGRAY);
            DrawText("Built with SCons", 10, 35, 16, GRAY);

            // Draw wire
            DrawLineEx(wireStart, wireEnd, 4.0f, DARKGRAY);

            // Draw battery
            Vector2 batteryPos = { 50, SCREEN_HEIGHT / 2.0f };
            DrawRectangle(batteryPos.x - 5, batteryPos.y - 20, 10, 40, RED);
            DrawRectangle(batteryPos.x - 3, batteryPos.y - 15, 6, 5, DARKGRAY);
            DrawText("+", batteryPos.x - 15, batteryPos.y - 30, 20, RED);
            DrawText("-", batteryPos.x - 15, batteryPos.y + 15, 20, BLUE);

            // Draw resistor
            Vector2 resistorPos = { SCREEN_WIDTH - 50, SCREEN_HEIGHT / 2.0f };
            DrawRectangle(resistorPos.x - 10, resistorPos.y - 15, 20, 30, ORANGE);
            DrawText("R", resistorPos.x - 5, resistorPos.y - 5, 12, WHITE);

            // Draw electron
            DrawCircleV(electron.position, electron.radius, electron.color);
            DrawCircleV(electron.position, electron.radius - 2, Fade(WHITE, 0.5f));

            // Draw trail
            for (int i = 0; i < 5; i++) {
                float trailT = t - (i * 0.05f);
                if (trailT < 0) trailT += 1.0f;
                Vector2 trailPos = {
                    wireStart.x + (wireEnd.x - wireStart.x) * trailT,
                    wireStart.y + sin((animationTime - i * 0.1f) * 3.0f) * 20.0f
                };
                DrawCircleV(trailPos, electron.radius * 0.5f, Fade(electron.color, 0.3f - i * 0.05f));
            }

            DrawText(TextFormat("FPS: %d", GetFPS()), 10, SCREEN_HEIGHT - 30, 20, GREEN);
            DrawText("Press ESC to exit", SCREEN_WIDTH - 150, SCREEN_HEIGHT - 30, 20, DARKGRAY);

        EndDrawing();
    }

    CloseWindow();

    printf("Program exited normally\n");

    return 0;
}
