FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
WORKDIR /src

COPY *.sln .
COPY SatelliteTracker/*.csproj ./SatelliteTracker/
RUN dotnet restore

COPY SatelliteTracker/.  ./SatelliteTracker/
WORKDIR /src/SatelliteTracker
RUN dotnet publish -c Release -o /app/publish

FROM mcr.microsoft,com/dotnet/sdk:7.0 as runtime
WORKDIR /app

COPY --from=build /app/publish ./

COPY SatelliteTracker/Nmea_src/output.nmea ./Nmea_src/output.nmea

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENV ASPNETCORE_URLS=http://+:8000 \
    DOTNET_RUNNNG_IN_CONTAINER=true \ 
    SimulationMode=true \
    SimulationDataFilePath=Nmea_src/output.nmea
    
EXPOSE 8000

ENTRYPOINT [ "/entrypoint.sh" ]_