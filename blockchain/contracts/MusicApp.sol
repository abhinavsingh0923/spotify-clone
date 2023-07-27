// SPDX-License-Identifier: MIT 
pragma solidity >=0.4.22 <0.9.0;

contract MusicApp{
    struct MusicTrack{
        string name;
        string artist;
        string song;
    }

    mapping (uint256 => MusicTrack) public musictracks;
    uint256 public trackcounter;

    event TrackUploaded(uint256 trackId, string name, string artist,  string song);


    function uploadTrack(string memory _name, string memory _artist, string memory _song) public {
        trackcounter++;
        musictracks[trackcounter] = MusicTrack(_name, _artist, _song);
        emit TrackUploaded(trackcounter, _name, _artist, _song);
    }

    function getMusicTrack(uint256 trackId) public view returns(string memory, string memory, string memory){
        MusicTrack memory tracks = musictracks[trackId];
        return (tracks.name, tracks.artist, tracks.song);
    }

    function getTotalTracks() public view returns(uint256){
        return trackcounter;
    }
}